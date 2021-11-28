<script>
	import Navbar from '../components/navbar.svelte';

	let current_question = 0;

	let questions = [
		{
			content: 'Hello, world',
			type: 'IT'
		},

		{
			content: 'Hello, world',
			type: 'IT'
		},

		{
			content: 'Hello, world',
			type: 'IT'
		},

		{
			content: 'Hello, world',
			type: 'IT'
		},

		{
			content: 'Hello, world',
			type: 'IT'
		},

		{
			content: 'Hello, world',
			type: 'IT'
		},

		{
			content: 'Hello, world',
			type: 'IT'
		}
	];

	let num_of_question = questions.length;

	let scores = {
		IT: 0,
		Business: 0,
		Language: 0,
		Graphics: 0
	};

	let selected = [];

	function addScore(score) {
		scores[questions[current_question].type] += score - (selected[current_question] | 0);
		if (selected[current_question]) {
			document.querySelector(
				`.right .selection:nth-child(${6 - selected[current_question]}) .square div`
			).style.backgroundColor = 'transparent';
		}
		selected[current_question] = score;
		const colors = ['#01bd10', '#8dd100', '#f8c400', '#fc9700', '#fd3100'];
		document.querySelector(
			`.right .selection:nth-child(${6 - score}) .square div`
		).style.backgroundColor = colors[5 - score];
	}

	let prev_btn, next_btn, submit_btn;

	function prev() {
		current_question--;
		next_btn.style.display = 'block';
		submit_btn.style.display = 'none';
		if (current_question == 0) prev_btn.disabled = true;
	}

	function next() {
		current_question++;
		prev_btn.disabled = false;
		if (current_question == num_of_question - 1) {
			next_btn.style.display = 'none';
			submit_btn.style.display = 'block';
		}
	}

	function submit() {
		console.log('submit');
	}
</script>

<Navbar />

<main>
	<div class="grid-container">
		<div class="left">
			<p>{current_question + 1}</p>
		</div>
		<div class="mid">
			<p>{questions[current_question].content}</p>
		</div>
		<div class="right">
			<button class="selection" on:click={() => addScore(5)}>
				<div class="square">
					<div />
				</div>
				Hoàn toàn đúng
			</button>
			<button class="selection" on:click={() => addScore(4)}>
				<div class="square">
					<div />
				</div>
				Thường là đúng
			</button>
			<button class="selection" on:click={() => addScore(3)}>
				<div class="square">
					<div />
				</div>
				Không rõ ràng
			</button>
			<button class="selection" on:click={() => addScore(2)}>
				<div class="square">
					<div />
				</div>
				Thường là sai
			</button>
			<button class="selection" on:click={() => addScore(1)}>
				<div class="square">
					<div />
				</div>
				Hoàn toàn sai
			</button>
		</div>
	</div>
	<div class="n-btn-container">
		<button class="n-btn" bind:this={prev_btn} on:click={prev} disabled>Previous</button>
		<button class="n-btn" bind:this={next_btn} on:click={next}>Next</button>
		<button class="n-btn" bind:this={submit_btn} on:click={submit} style="display: none"
			>Submit</button
		>
	</div>
	<div class="progress-container">
		{#each Array(num_of_question) as _, i}
			{#if i != current_question}
				<button on:click={() => (current_question = i)} />
			{:else}
				<button on:click={() => (current_question = i)} class="current" />
			{/if}
		{/each}
	</div>
</main>

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
		font-weight: 800;
		font-size: 1.2rem;
		text-align: center;
		width: 100%;
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
</style>
