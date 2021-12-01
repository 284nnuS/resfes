<script>
	import Navbar from '../components/navbar.svelte';
	import { onMount } from 'svelte';
	import { Base64 } from 'js-base64';

	let dragarea;

	onMount(async () => {
		['dragenter', 'dragover', 'dragleave', 'drop'].forEach((eventName) => {
			dragarea.addEventListener(eventName, preventDefaults, false);
		});

		['dragenter', 'dragover'].forEach((eventName) => {
			dragarea.addEventListener(eventName, highlight, false);
		});
		['dragleave', 'drop'].forEach((eventName) => {
			dragarea.addEventListener(eventName, unhighlight, false);
		});
	});

	function highlight(e) {
		dragarea.classList.add('highlight');
	}

	function unhighlight(e) {
		dragarea.classList.remove('highlight');
	}

	function preventDefaults(e) {
		e.preventDefault();
		e.stopPropagation();
	}

	function handleDrop(e) {
		let dt = e.dataTransfer;
		let files = dt.files;
		if (files.length > 0) {
			//`
		}
		let reader = new FileReader();
		reader.onload = function (event) {
			let buffer = event.target.result;
			let arr = new Uint8Array(buffer);
			let b64str = Base64.fromUint8Array(arr);
			console.log(b64str);
		};
		reader.readAsArrayBuffer(files[0]);
	}
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
				<img src="/image 3.png" alt="3" />
				<img src="/image 4.png" alt="4" />
				<img src="/image 5.png" alt="5" />
			</div>
		</div>
		<div id="drop-area" bind:this={dragarea} on:drop={handleDrop}>
			<img src="/upload.png" alt="Upload" />
			<p>No file chosen, yet!</p>
		</div>
	</div>
	<button id="upload-btn">UPLOAD</button>
	<div class="icon-container">
		<div>
			<img src="/icon1.png" alt="1" />
		</div>
		<div>
			<img src="/icon2.png" alt="2" />
		</div>
		<div>
			<img src="/icon5.png" alt="3" />
		</div>
		<div>
			<img src="/icon3.png" alt="4" />
		</div>
		<div>
			<img src="/icon4.png" alt="5" />
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

	#drop-area {
		width: 12rem;
		aspect-ratio: 124/171;
		border: 2px dashed white;
		border-radius: 1.5rem;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	#drop-area img {
		width: 7rem;
	}

	#drop-area p {
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
		margin: 1rem;
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
