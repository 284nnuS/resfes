<script>
	import Navbar from '../components/navbar.svelte';
	import { onMount } from 'svelte';
	import axios from 'axios';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import Footer from '../components/footer.svelte';
	import Error from '../components/error.svelte';

	const id = $page.query.get('id');

	let errmessage;
	let ready;

	let current_question = 0;

	let questions;

	if (id)
		onMount(async () => {
			axios
				.get(`/api/quiz/${id}`)
				.then((response) => {
					if (response.data.success) questions = response.data.result;
					else errmessage = response.data.message;
				})
				.catch(function (reason) {
					errmessage = reason.message;
				})
				.finally(() => (ready = true));
		});
	else {
		errmessage = 'Invalid request, please try again';
		ready = true;
	}

	let scores = {
		it: 0,
		business: 0,
		language: 0,
		graphics: 0
	};

	let selected = [];

	function addScore(score) {
		scores[questions[current_question].type] += score - (selected[current_question] | 0);
		selected[current_question] = score;
	}

	function submit() {
		axios
			.post(`/api/submit`, {
				id: id,
				scores: [scores.it, scores.business, scores.graphics, scores.language]
			})
			.then((response) => {
				if (response.data.success) {
					goto(`/result?id=${id}`);
				}
			})
			.catch(function (reason) {
				errmessage = reason.message;
			});
	}
</script>

<svelte:head>
	<title>Quiz</title>
</svelte:head>

{#if !errmessage && ready}
	<Navbar />
	<main>
		{#if questions}
			<div class="grid-container">
				<div class="left">
					<p>{current_question + 1}</p>
				</div>
				<div class="mid">
					<p>{questions[current_question].content}</p>
				</div>
				<div class="right">
					<button class="selection" on:click={() => addScore(5)}>
						{#if selected[current_question] === 5}
							<div class="square" style="background-color: #01bd10">
								<div />
							</div>
						{:else}
							<div class="square">
								<div />
							</div>
						{/if}
						Hoàn toàn đúng
					</button>
					<button class="selection" on:click={() => addScore(4)}>
						{#if selected[current_question] === 4}
							<div class="square" style="background-color: #8dd100">
								<div />
							</div>
						{:else}
							<div class="square">
								<div />
							</div>
						{/if}
						Thường là đúng
					</button>
					<button class="selection" on:click={() => addScore(3)}>
						{#if selected[current_question] === 3}
							<div class="square" style="background-color: #f8c400">
								<div />
							</div>
						{:else}
							<div class="square">
								<div />
							</div>
						{/if}
						Không hẳn đúng
					</button>
					<button class="selection" on:click={() => addScore(2)}>
						{#if selected[current_question] === 2}
							<div class="square" style="background-color: #fc9700">
								<div />
							</div>
						{:else}
							<div class="square">
								<div />
							</div>
						{/if}
						Có vẻ sai
					</button>
					<button class="selection" on:click={() => addScore(1)}>
						{#if selected[current_question] === 1}
							<div class="square" style="background-color: #fd3100">
								<div />
							</div>
						{:else}
							<div class="square">
								<div />
							</div>
						{/if}
						Thường là sai
					</button>
				</div>
			</div>
			<div class="n-btn-container">
				{#if current_question > 0}
					<button class="n-btn" on:click={() => current_question--}>Lùi lại</button>
				{:else}
					<button class="n-btn" disabled>Lùi lại</button>
				{/if}
				{#if current_question < questions.length - 1}
					<button class="n-btn" on:click={() => current_question++}>Tiếp theo</button>
				{:else if selected.reduce((acc, cv) => (cv ? acc + 1 : acc), 0) === questions.length}
					<button class="n-btn" on:click={submit}>Gửi</button>
				{:else}
					<button class="n-btn" disabled>Gửi</button>
				{/if}
			</div>
			<div class="progress-container">
				{#each Array(questions.length) as _, i}
					{#if i === current_question}
						<button on:click={() => (current_question = i)} class="current" />
					{:else if selected[i]}
						<button on:click={() => (current_question = i)} class="selected" />
					{:else}
						<button on:click={() => (current_question = i)} />
					{/if}
				{/each}
			</div>
		{/if}
	</main>
	<Footer />
{:else if ready}
	<main
		style="
		background-color: #fff;
		height: 100vh;
		padding: 0;
		gap: 1rem;
		"
	>
		<Error {errmessage} btnText="Take Me Back" callback={() => goto('/')} />
	</main>
{/if}

<style>
	main {
		background-color: #efb0c9;
		width: 100vw;
		padding-top: 8rem;
		padding-bottom: 5rem;
		height: calc(100vh - 5rem - 8rem);
		display: flex;
		align-items: center;
		flex-direction: column;
		justify-content: center;
		gap: 1rem;
	}

	button {
		cursor: pointer;
	}

	.grid-container {
		display: grid;
		grid-template-columns: 7rem 30% 14rem;
		grid-template-rows: 12.5rem;
		justify-content: center;
		width: 100%;
	}

	.left {
		background-color: #20519b;
		border-top-left-radius: 30px;
		border-bottom-left-radius: 30px;
	}

	.left p {
		font-weight: 700;
		font-size: 3.125rem;
		color: white;
		text-align: center;
		line-height: 12.5rem;
		margin: 0;
	}

	.mid {
		background-color: white;
	}

	.right {
		display: grid;
		grid-template-rows: repeat(5, calc(20% - 0.4rem));
		margin-left: 0.5rem;
		row-gap: 0.5rem;
	}
	.mid {
		display: flex;
		align-items: center;
	}
	.mid p {
		color: #4c70cc;
		font-weight: 700;
		font-size: 1.2rem;
		text-align: center;
		width: 100%;
		padding: 1rem;
	}

	.selection {
		background-color: white;
		border: 2px solid transparent;
		border-top-right-radius: 15px;
		border-bottom-right-radius: 15px;
		display: flex;
		align-items: center;
		color: #86a8ff;
		font-weight: 700;
		font-size: 1.1rem;
		padding: 0 0.5rem;
	}

	.n-btn-container {
		display: flex;
		justify-content: center;
		gap: 2rem;
	}

	.selection .square {
		width: 24px;
		height: 24px;
		border-radius: 20px;
		margin-right: 0.5rem;
		border: 2px solid transparent;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.selection .square div {
		width: 16px;
		height: 16px;
		border-radius: 10px;
	}

	.selection:nth-child(1) .square {
		border-color: #01bd10;
	}

	.selection:nth-child(2) .square {
		border-color: #8dd100;
	}

	.selection:nth-child(3) .square {
		border-color: #f8c400;
	}

	.selection:nth-child(4) .square {
		border-color: #fc9700;
	}

	.selection:nth-child(5) .square {
		border-color: #fd3100;
	}

	.n-btn {
		width: 13rem;
		height: 3.5rem;
		color: white;
		border-radius: 3.25rem;
		background-color: #7894dd;
		border: 0px solid transparent;
		margin: 1rem 0;
		font-size: 1.25rem;
		font-weight: 700;
	}

	.n-btn:hover {
		color: #fff;
		background-color: #6c86ca;
	}

	.n-btn:disabled {
		background-color: #929292;
	}

	.progress-container {
		display: flex;
		flex-direction: row;
		gap: 1rem;
	}

	.progress-container button {
		width: 30px;
		height: 30px;
		background-color: white;
		border: 2px solid transparent;
		border-radius: 30px;
	}
	.progress-container button:hover {
		border-color: #86a8ff;
	}

	.progress-container button.current {
		background-color: #86a8ff;
		border-color: white;
	}

	.progress-container button.current:hover {
		border-color: white;
	}

	.progress-container button.selected {
		background-color: #7a7a7a;
		border-color: white;
	}

	.progress-container button.selected:hover {
		border-color: white;
	}
</style>
