<script>
	export let color = '#ffffff';

	$: cssVarStyles = `--name-color:${color}`;
</script>

<div class="navbar" style={cssVarStyles}>
	<div class="navbar-left">
		<ul>
			<li class="team-name">
				ZOOMI<br />DSOON
			</li>
			<li>
				<a href="reason">Reason</a>
			</li>
			<li>
				<a href="about">About Us</a>
			</li>
		</ul>
	</div>
	<div class="navbar-right">
		<img src="/fptedu.png" class="nav-logo" alt="FPT Education Logo" />
		<img src="/resfes.png" class="nav-logo" alt="Resfes Logo" />
	</div>
</div>

<style>
	.navbar {
		position: fixed;
		height: 6rem;
		padding: 3rem 3rem 0 3rem;
		left: 0;
		right: 0;
		z-index: 100;
		display: flex;
		justify-content: space-between;
	}

	.navbar-left,
	.navbar-right {
		display: flex;
		align-items: center;
	}

	.navbar-left ul {
		list-style-type: none;
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding-left: 2.5vw;
		gap: calc(10vw - 1rem);
	}

	.navbar-left li {
		padding: 0;
	}

	.navbar-left ul li a {
		text-decoration: none;
		color: #fff;
		font-size: 1.5rem;
		display: block;
		padding: 0;
		display: block;
		font-weight: 800;
		width: 8rem;
		height: 4rem;
		line-height: 4rem;
		text-align: center;
	}

	.team-name {
		color: var(--name-color, white);
		font-weight: 700;
		font-size: 2rem;
		margin: 0;
	}

	.nav-logo {
		height: 4rem;
		margin-left: 3rem;
	}
</style>
