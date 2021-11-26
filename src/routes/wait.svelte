<script>
	import Navbar from '../components/navbar.svelte';
</script>

<Navbar />

<main>
	<div class="icon-container">
		<div>
			<div class="icon">
				<img src="/icon1.png" alt="Image 1" />
			</div>
			<div class="icon">
				<img src="/icon2.png" alt="Image 2" />
			</div>
		</div>
		<div class="message-container">
			<b> BẠN VUI LÒNG CHỜ TRONG GIÂY LÁT !</b>
			<b class="dot">. . .</b>
		</div>
		<div>
			<div class="icon">
				<img src="/icon3.png" alt="Image 4" />
			</div>
			<div class="icon">
				<img src="/icon4.png" alt="Image 5" />
			</div>
		</div>
	</div>
	<div class="container-button">
		<a href="/" class="home-btn">
			<button type="submit">Home</button>
		</a>
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
	center {
		width: 100%;
		height: 100%;
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

	.icon {
		background-color: #fff;
		border-radius: 5rem;
		width: 6rem;
		height: 6rem;
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 1.5rem;
		margin: 3rem;
	}

	.icon-container img {
		width: 100%;
		aspect-ratio: 1/1;
	}
	.message-container {
		width: 60rem;
		height: 20rem;
		background-color: white;
		color: #20519b;
		border-radius: 2rem;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		gap: 0.5rem;
	}
	.message-container b {
		text-align: center;
		font-size: xx-large;
		height: auto;
		margin: 0;
	}
</style>
