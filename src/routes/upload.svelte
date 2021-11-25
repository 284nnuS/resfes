<script>
	import Navbar from '../components/navbar.svelte';
</script>

<Navbar />
<main>
	<div class="top-container">
		<div class="column-left">
			<p style="background-color: #fff; color: #86A8FF">
				Note: Portrait photos have a full face, so avoid photos with a slanted face angle as well as
				not too blurry or too small. Example:
			</p>
			<div class="img-container">
				<img src="/image 3.png" alt="Image 1" />
				<img src="/image 4.png" alt="Image 2" />
				<img src="/image 5.png" alt="Image 3" />
			</div>
		</div>
		<div id="upload-container">
			<img src="/upload.png" alt="Upload" />
			<p>No file chosen, yet!</p>
		</div>
	</div>
	<button id="upload-btn">UPLOAD</button>
	<div class="icon-container">
		<div>
			<img src="/icon1.png" alt="Image 1" />
		</div>
		<div>
			<img src="/icon2.png" alt="Image 2" />
		</div>
		<div>
			<img src="/icon5.png" alt="Image 3" />
		</div>
		<div>
			<img src="/icon3.png" alt="Image 4" />
		</div>
		<div>
			<img src="/icon4.png" alt="Image 5" />
		</div>
	</div>
</main>

<style>
	main {
		background-color: #efb0c9;
		width: 100vw;
		padding-top: 8rem;
		margin-bottom: 5rem;
		height: calc(100vh - 5rem - 8rem);
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}

	.top-container {
		display: flex;
		align-items: center;
		gap: 2rem;
	}

	.column-left {
		width: 30rem;
	}

	.column-left p {
		border-radius: 30px;
		padding: 1rem 2rem;
		font-weight: 500;
		font-size: 1.25rem;
		margin-top: 0;
	}

	.img-container {
		display: flex;
		justify-content: space-around;
		width: 100%;
	}

	.img-container img {
		width: 7em;
		aspect-ratio: 124/171;
		border: 5px solid white;
	}

	#upload-btn {
		width: 13rem;
		height: 3.5rem;
		color: #86a8ff;
		border-radius: 3.25rem;
		background-color: #fff;
		border: 0px solid transparent;
		margin: 1rem 0;
		font-size: 1.25rem;
		font-weight: 700;
	}

	#upload-btn:hover {
		color: #fff;
		background-color: #86a8ff;
	}

	#upload-container {
		width: 12rem;
		aspect-ratio: 124/171;
		border: 2px dashed white;
		border-radius: 1.5rem;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	#upload-container img {
		width: 7rem;
	}

	#upload-container p {
		font-size: 1.3rem;
		font-weight: 400;
		color: white;
		padding: 0.5rem;
		text-align: center;
	}

	.icon-container {
		display: flex;
		align-items: center;
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
		margin:1rem;
	}

	.icon-container div:nth-child(3) {
		width: 7rem;
		height: 7rem;
		background-color: #b8d7db;
	}

	.icon-container img {
		width: 100%;
		aspect-ratio: 1/1;
	}

	@media only screen and (max-height: 800px) {
		.icon-container {
			display: none;
		}
	}
</style>
