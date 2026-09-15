export default function Navbar(){
	return (
		<nav className="flex fixed top-0 left-0 right-0 h-30  bg-[#26351F] color-[#FFF8E7]">
			<div className="items-center h-full w-1/5 flex">
				<a className="hover-scale-105 flex text-center w-full justify-center">
					GrepShip
				</a>
			</div>
			<div>
				<input className="" type="text"/>
			</div>
		</nav>
	)
}
