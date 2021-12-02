<script>
	import Navbar from '../components/navbar.svelte';
	import { onMount } from 'svelte';
	import { Base64 } from 'js-base64';
	import { goto, invalidate, prefetch, prefetchRoutes } from '$app/navigation';
	import axios from 'axios';
	import { fade } from 'svelte/transition';
	import Footer from '../components/footer.svelte';
	import Error from '../components/error.svelte';

	let dragarea;
	let imgb64;
	let ext;

	let state = 'none';
	let errmessage;

	let file_input;

	$: dataurl = `data:image/${ext};base64,${imgb64}`;

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

	function handleFile(files) {
		if (files.length > 0) {
			state = 'error';
			errmessage = 'Please select only one image file';
			return;
		}
		let file = files[0];

		if (!['image/gif', 'image/jpeg', 'image/png'].includes(file.type)) {
			state = 'error';
			errmessage = 'Please select only one image file';
			return;
		}

		ext = file.name.split('.').pop();
		let reader = new FileReader();
		reader.onload = function (event) {
			let buffer = event.target.result;
			let arr = new Uint8Array(buffer);
			imgb64 = Base64.fromUint8Array(arr);
		};
		reader.readAsArrayBuffer(files[0]);
	}

	function upload() {
		state = 'uploading';
		axios
			.post('/api/analyze', {
				payload: imgb64
			})
			.then(function (response) {
				console.log(response.data);
				if (response.data.success) {
					goto(`/quiz?id=${response.data.id}`);
				} else {
					setTimeout(() => {
						errmessage = response.data.message;
						state = 'error';
					}, 1000);
				}
			})
			.catch(function (reason) {
				errmessage = reason.message;
				state = 'error';
			});
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
				<img src="/image 3.jpg" alt="" />
				<img src="/image 4.jpg" alt="" />
				<img src="/image 5.jpg" alt="" />
			</div>
		</div>
		<input
			type="file"
			bind:this={file_input}
			style="display:none;"
			on:change={() => handleFile(file_input.files)}
		/>
		<button
			type="file"
			id="drop-area"
			bind:this={dragarea}
			on:drop={(e) => handleFile(e.dataTransfer.files)}
			on:click={() => file_input.click()}
		>
			{#if !imgb64}
				<img src="/upload.png" alt="" />
				<p>No file chosen, yet!</p>
			{:else}
				<img src={dataurl} id="uploaded-img" alt="" />
			{/if}
		</button>
	</div>
	{#if imgb64}
		<button id="upload-btn" on:click={upload}>UPLOAD</button>
	{:else}
		<button id="upload-btn" disabled>UPLOAD</button>
	{/if}
	<div class="icon-container">
		<div>
			<img src="/icon1.png" alt="" />
		</div>
		<div>
			<img src="/icon2.png" alt="" />
		</div>
		<div>
			<img src="/icon5.png" alt="" />
		</div>
		<div>
			<img src="/icon3.png" alt="" />
		</div>
		<div>
			<img src="/icon4.png" alt="" />
		</div>
	</div>

	{#if state !== 'none'}
		<div id="modal-container" in:fade={{ duration: 500 }} out:fade={{ duration: 500 }}>
			{#if state === 'uploading'}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					style="margin: auto; background: rgba(0, 0, 0, 0) none repeat scroll 0% 0%; display: block; shape-rendering: auto;"
					width="150px"
					height="150px"
					viewBox="20 20 60 60"
					preserveAspectRatio="xMidYMid"
				>
					<g transform="rotate(0 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#fe718d">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.9230769230769231s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(27.692307692307693 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#f47e60">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.8461538461538461s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(55.38461538461539 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#f8b26a">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.7692307692307693s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(83.07692307692308 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#abbd81">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.6923076923076923s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(110.76923076923077 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#849b87">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.6153846153846154s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(138.46153846153845 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#6492ac">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.5384615384615384s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(166.15384615384616 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#637cb5">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.46153846153846156s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(193.84615384615384 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#6a63b6">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.38461538461538464s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(221.53846153846155 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#fe718d">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.3076923076923077s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(249.23076923076923 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#f47e60">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.23076923076923078s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(276.9230769230769 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#f8b26a">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.15384615384615385s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(304.61538461538464 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#abbd81">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="-0.07692307692307693s"
								repeatCount="indefinite"
							/>
						</rect>
					</g><g transform="rotate(332.3076923076923 50 50)">
						<rect x="46.5" y="22.5" rx="3.5" ry="5.5" width="7" height="11" fill="#849b87">
							<animate
								attributeName="opacity"
								values="1;0"
								keyTimes="0;1"
								dur="1s"
								begin="0s"
								repeatCount="indefinite"
							/>
						</rect>
					</g>
				</svg>
				<p>Processing your image</p>
			{:else if state === 'error'}
				<Error {errmessage} btnText="OK" callback={() => (state = 'none')} color="white" />
			{/if}
		</div>
	{/if}
</main>
<Footer />

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

	#upload-btn:disabled {
		color: #fff;
		background-color: #929292;
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
		padding: 1rem;
		background-color: transparent;
		cursor: pointer;
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
		margin: 0;
	}

	#uploaded-img {
		width: 100% !important;
		height: 100%;
		object-fit: contain;
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

	#modal-container {
		position: fixed;
		background-color: rgba(60, 60, 60, 0.5);
		z-index: 100;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 1rem;
	}

	#modal-container svg {
		margin: 0 !important;
	}

	#modal-container p {
		color: white;
		font-weight: 700;
		margin: 0;
		font-size: 1.5rem;
	}
</style>
