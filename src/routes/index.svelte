<script>
	import Navbar from '../components/navbar.svelte';
	import Footer from '../components/footer.svelte';
</script>

<Navbar color="#2d3e69" />
<main>
	<div class="half-circle-container">
		<div class="half-circle" />
		<a href="/upload" class="play-link">
			<img src="/play.png" alt="" />
		</a>
		<div class="icon" id="icona">
			<img src="/icon1.png" alt="" />
		</div>
		<div class="icon" id="iconb">
			<img src="/icon2.png" alt="" />
		</div>
		<div class="icon" id="iconc">
			<img src="/icon3.png" alt="" />
		</div>
		<div class="icon" id="icond">
			<img src="/icon4.png" alt="" />
		</div>
	</div>

	<div class="left-container">
		<h2>ỨNG DỤNG <br/> TƯ VẤN NGÀNH HỌC</h2>
		<p>
			Ứng dụng của chúng tôi sử dụng AI phân tích khuôn mặt kết hợp với các câu hỏi dựa trên
			Thuyết đa trí tuệ để hỗ trợ tư vấn ngành học phù hợp với bạn tại Đại học FPT.
		</p>
		<a href="upload" class="start-btn">
			<button type="submit">Bắt đầu</button>
		</a>
	</div>
</main>
<Footer />

<svelte:head>
	<title>Trang chủ</title>
</svelte:head>

<style>
	main {
		margin-bottom: 5rem;
		margin-top: 6rem;
	}

	button {
		cursor: pointer;
	}

	.half-circle-container {
		position: relative;
		margin-left: 15.46875vw;
		margin-top: -14rem;
		width: 91.875vw;
	}
	.half-circle {
		position: relative;
		width: 100%;
		aspect-ratio: 2/1;
		background-color: #efb0c9;
		border-top: 0;
		border-bottom-left-radius: 91.875vw;
		border-bottom-right-radius: 91.875vw;
		z-index: -1;
		padding-bottom: 0rem;
		margin-bottom: 4.5rem;
	}
	.play-link {
		position: absolute;
		display: block;
		bottom: -3rem;
		z-index: 5;
		background-color: #eee;
		border-radius: 5rem;
		margin: auto auto 0 auto;
		left: 0;
		right: 0;
		width: 10rem;
		height: 10rem;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.play-link img {
		width: 9rem;
		height: 9rem;
	}

	.icon {
		width: 10rem;
		height: 10rem;
		border-radius: 5rem;
		z-index: 5;
		background-color: #fff;
		position: absolute;
		margin: auto auto 0 auto;
		display: flex;
		justify-content: center;
		align-items: center;
		bottom: 0;
	}

	.icon img {
		width: 7rem;
		height: 7rem;
	}
	#icona {
		bottom: calc(15rem * 0.30901699437 - 1rem);
		left: calc(15rem * -0.95105651629);
		right: calc(15rem * 0.95105651629);
	}

	#icona img {
		width: 6rem;
		height: 6rem;
	}

	#iconb {
		bottom: calc(15rem * 0.91354545764 - 1rem);
		left: calc(15rem * -0.40673664307);
		right: calc(15rem * 0.40673664307);
	}
	#iconc {
		bottom: calc(15rem * 0.91354545764 - 1rem);
		left: calc(15rem * 0.40673664307);
		right: calc(15rem * -0.40673664307);
	}
	#icond {
		bottom: calc(15rem * 0.30901699437 - 1rem);
		left: calc(15rem * 0.95105651629);
		right: calc(15rem * -0.95105651629);
	}

	.left-container {
		position: absolute;
		bottom: 5rem;
		padding: 2rem;
		padding-right: 0;
		width: 30vw;
		height: 60vh;
		justify-content: center;
		display: flex;
		flex-direction: column;
		margin-top: 5rem;
		gap: 0.5rem;
	}

	.left-container h2,
	p {
		margin: 0;
		padding: 0;
	}

	.left-container h2 {
		font-size: 2rem;
		hyphens: manual;
		font-weight: 800;
		color: #ca608b;
		width: 75%;
	}

	.left-container p {
		font-size: 1rem;
		font-weight: 500;
		padding-right: 5rem;
		color: black;
	}

	.start-btn {
		align-self: center;
		margin-top: 2rem;
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
</style>
