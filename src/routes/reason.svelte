<script>
	import Navbar from '../components/navbar.svelte';
	import Footer from '../components/footer.svelte';
</script>

<Navbar />

<main>
	<div class="container">
		<p>
			Một lần nữa xin cảm ơn bạn đã tin tưởng và sử dụng ứng dụng của Zoomi Team! Có thể nói để
			chuẩn bị cho vòng chung kết Research Festival 2021, bọn tớ đã bỏ ra không ít công sức để hoàn
			thiện sản phẩm sớm nhất có thể. Đối với chúng tớ, sản phẩm này không chỉ đơn giản là một thành
			phẩm để dự thi, nó còn như một đứa con tinh thần được dồn vào rất nhiều tâm huyết và chứa đựng
			từng dấu nét riêng của mỗi thành viên trong đội. Vì thời gian gấp rút song song với chương
			trình học dày đặc, chúng tớ biết rằng ứng dụng này vẫn còn tồn tại nhiều thiếu sót cần được
			khắc phục. Vì thế Zoomi Team luôn luôn hoan nghênh mọi ý kiến đóng góp và phản hồi của các
			bạn. Nhờ vào đó chúng tớ sẽ tiếp tục nghiên cứu, không ngừng cải thiện và đổi mới để mang lại
			trải nghiệm tốt nhất cho người dùng. Hy vọng với kết quả trả về từ ứng dụng, các bạn sẽ nhận
			được lời khuyên hữu ích để có thể đưa ra được lựa chọn phù hợp nhất cho ngành học của mình.
			Thank you!
		</p>
	</div>
	<div class="container-button">
		<a href="/" class="home-btn">
			<button type="submit">Trang chủ</button>
		</a>
	</div>
</main>
<Footer />

<svelte:head>
	<title>Đôi lời</title>
</svelte:head>

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
		width: 70%;
		border-radius: 2rem;
		flex-direction: column;
		display: flex;
		justify-content: center;
	}

	.container p {
		font-size: 1.5rem;
		text-align: justify;
		padding: 1.5rem;
		font-weight: 600;
		color: white;
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
