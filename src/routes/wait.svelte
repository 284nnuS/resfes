<script>
	import Navbar from '../components/navbar.svelte';
</script>

<Navbar />

<main>
	<center>
		<div class="icon-container">
			<div>
				<div class="icon">
					<img src="/icon1.png" alt="Image 1" />
				</div>
				<div class="icon">
					<img src="/icon2.png" alt="Image 2" />
				</div>
			</div>
			<div class="container">
				<div class="container-message">
					<b>
                    <br />
						<br />
						BẠN VUI LÒNG CHỜ TRONG GIÂY LÁT !</b
					>
					<br />
					<br />
                    <br />
                    <br />
					<b class="dot">.          .          .</b>
				</div>
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
			<a href="/" class="start-btn">
				<button type="submit">Home</button>
			</a>
		</div>
	</center>
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
	}
	center {
		width: 100%;
		height: 100%;
	}
	.container-button {
		padding: 5px;
		justify-content: bottom;
	}
	.start-btn {
		align-self: center;
		margin-top: 0.5rem;
	}

	.start-btn button {
		width: 13rem;
		height: 3.5rem;
		color: #fff;
		background-color: #d184a3;
		border: 0;
		font-size: 1.5rem;
		font-weight: 700;
		border-radius: 5rem;
	}

	.start-btn button:hover {
		background-color: rgb(223, 149, 180);
		color: #fff;
		transition: color 0.3s ease-in;
	}

	.icon-container {
		width: 90%;
		height: 80%;
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
	.container {
		width: 80%;
		height: 70%;
	}
	.container-message {
		width: 60%;
		height: 80%;
		background-color: white;
        color:#20519B;
		border-radius: 2rem;
		padding: 1rem;
	}
	.container-message b {
		margin: 1rem;
		text-align: center;
		font-size: xx-large;
	}

	@media only screen and (max-height: 800px) {
		.icon-container {
			display: none;
		}
	}
</style>
