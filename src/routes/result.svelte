<script>
	import Navbar from '../components/navbar.svelte';
</script>

<Navbar />

<main>
	<div class="content">
		<b> LEVELS OF FITNESS FOR MAJORS THROUGH FACE ANALYSIS </b>
	</div>
	<div class="container-result">
		<div class="container-result-small">
			<div class="round-icon" />
			<div class="square-result" />
		</div>
		<div class="container-result-small">
			<div class="round-icon" />
			<div class="square-result" />
		</div>
		<div class="container-result-small">
			<div class="round-icon" />
			<div class="square-result" />
		</div>
		<div class="container-result-small">
			<div class="round-icon" />
			<div class="square-result" />
		</div>
	</div>
	<div class="container-button">
		<a href="/" class="home-btn">
			<button type="submit">Home</button>
		</a>
	</div>
	<div class="icon-container">
		<div>
			<img src="/icon1.png" alt="1" />
		</div>
		<div>
			<img src="/icon2.png" alt="2" />
		</div>
		<div>
			<img src="/icon3.png" alt="3" />
		</div>
		<div>
			<img src="/icon4.png" alt="4" />
		</div>
	</div>
</main>

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

		width: 88px;

		height: 88px;

		border-radius: 50%;

		background-color: blue;

		border: 2px solid #000;

		left: 55%;

		transform: translate(-50%, -50%);
	}

	.square-result {
		width: 172px;

		height: 160px;

		border-radius: 15%;

		background-color: aqua;

		border: 2px solid #000;
	}

	@media only screen and (max-height: 800px) {
		.icon-container {
			display: none;
		}
	}
</style>
