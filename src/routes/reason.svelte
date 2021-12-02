<script>
	import Navbar from '../components/navbar.svelte';
	import Footer from '../components/footer.svelte';
</script>

<Navbar />

<main>
	<div class="container" />
	<div class="container-button">
		<a href="/" class="home-btn">
			<button type="submit">Home</button>
		</a>
	</div>
</main>
<Footer />

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

	.container {
		width: 60rem;
		height: 25rem;
		background-color: white;
		border-radius: 2rem;
		border: 6px solid #20519b;
	}
	.container-button {
		padding: 5px;
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
</style>
