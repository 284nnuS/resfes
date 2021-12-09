<script>
	import Navbar from '../components/navbar.svelte';
	import axios from 'axios';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import Footer from '../components/footer.svelte';
	import Error from '../components/error.svelte';
	import { goto, invalidate, prefetch, prefetchRoutes } from '$app/navigation';

	let id = $page.query.get('id');
	let errmessage;
	let ready = false;
	let result;

	if (id)
		onMount(async () => {
			axios
				.get(`/api/view/${id}`)
				.then((response) => {
					if (response.data.success) result = response.data.result;
					else errmessage = response.data.message;
				})
				.catch((error) => {
					errmessage = '?';
				})
				.finally(() => (ready = true));
		});
	else {
		errmessage = 'Invalid request, please try again';
		ready = true;
	}
</script>

{#if !errmessage && ready}
	<Navbar />
	<main>
		{#if result}
			<div class="content">
				<b>MỨC ĐỘ PHÙ HỢP VỚI CÁC NGÀNH HỌC THÔNG QUA PHÂN TÍCH KHUÔN MẶT</b>
			</div>
			<div class="container-result">
				<div class="container-result-small">
					<div class="round-icon">
						<img src="/it.png" alt="" />
					</div>
					<div class="square-result">
						<p>{Math.round(result[0] * 10) / 10}%</p>
						IT
					</div>
				</div>
				<div class="container-result-small">
					<div class="round-icon">
						<img src="/business.png" alt="" />
					</div>
					<div class="square-result">
						<p>{Math.round(result[1] * 10) / 10}%</p>
						Kinh tế
					</div>
				</div>
				<div class="container-result-small">
					<div class="round-icon">
						<img src="/graphic.png" alt="" />
					</div>
					<div class="square-result">
						<p>{Math.round(result[2] * 10) / 10}%</p>
						Đồ họa
					</div>
				</div>
				<div class="container-result-small">
					<div class="round-icon">
						<img src="/language.png" alt="" />
					</div>
					<div class="square-result">
						<p>{Math.round(result[3] * 10) / 10}%</p>
						Ngôn ngữ
					</div>
				</div>
			</div>
			<div class="container-button">
				<a href="/" class="home-btn">
					<button type="submit">Trang chủ</button>
				</a>
			</div>
			<div class="icon-container">
				<div>
					<img src="/icon1.png" alt="" />
				</div>
				<div>
					<img src="/icon2.png" alt="" />
				</div>
				<div>
					<img src="/icon3.png" alt="" />
				</div>
				<div>
					<img src="/icon4.png" alt="" />
				</div>
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
		margin-bottom: 6rem;
		height: calc(100vh - 6rem - 8rem);
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
	button {
		cursor: pointer;
	}
	.container-button {
		padding: 5px;
		justify-content: bottom;
	}
	.home-btn {
		align-self: center;
		margin-top: 0.5rem;
	}

	.home-btn button {
		width: 13rem;
		height: 3.5rem;
		color: #fff;
		background-color: #d184a3;
		border: 0;
		font-size: 1.5rem;
		font-weight: 700;
		border-radius: 5rem;
		cursor: pointer;
	}

	.home-btn button:hover {
		background-color: rgb(223, 149, 180);
		color: #fff;
		transition: color 0.3s ease-in;
	}
	.icon-container {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.icon-container div {
		background-color: #fff;
		border-radius: 5rem;
		width: 6rem;
		height: 6rem;
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 1.5rem;
		margin: 1rem;
	}

	.icon-container img {
		width: 100%;
		aspect-ratio: 1/1;
	}
	.content {
		height: 50px;
		background-color: #20519b;
		width: 55%;
		font-size: x-large;
		text-align: center;
		display: flex;
		justify-content: center;
		align-items: center;
		border-radius: 25px;
		color: white;
	}
	.container-result {
		margin-top: 5rem;
		width: 80%;
		display: flex;
		justify-content: center;
	}
	.container-result-small {
		margin: 2rem;
		position: relative;
		width: 160px;
	}

	.round-icon {
		position: absolute;
		width: 5.5rem;
		height: 5.5rem;
		border-radius: 50%;
		border: 3px solid #714992;
		background-color: white;
		left: 57.5%;
		transform: translate(-50%, -50%);
		padding: 1rem;
	}

	.round-icon img {
		width: 100%;
		height: 100%;
		object-fit: contain;
	}

	.square-result {
		width: 11rem;
		height: 9rem;
		border-radius: 15%;
		border: 5px solid #20519b;
		background-color: white;
		padding-top: 2rem;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		color: #20519b;
		font-weight: 600;
		font-size: 1.25rem;
	}

	.square-result p {
		color: #20519b;
		font-weight: 700;
		font-size: 3.25rem;
		margin: 0;
	}

	@media only screen and (max-height: 800px) {
		.icon-container {
			display: none;
		}
	}
</style>
