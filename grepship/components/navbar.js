export default function Navbar(){
	return (
		<nav className="flex fixed top-0 left-0 right-0 h-30  bg-[#26351F] color-[#FFF8E7]">
			<div className="items-center h-full w-1/5 flex">
				<a className="hover-scale-105 flex text-center w-full justify-center">
					GrepShip
				</a>
			</div>
			<div className="flex items-center justify-center w-1/3">
				<input className="pl-3 pr-10 bg-[#35452C] rounded-xl w-full h-1/3" placeholder="Harvest Friend" type="text"/>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					className="w-5 h-5 relative  right-7 h-full flex items-center justify-center text-gray-400"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						strokeLinecap="round"
						strokeLinejoin="round"
						strokeWidth="2"
						d="M21 21l-4.35-4.35M17 11a6 6 0 11-12 0 6 6 0 0112 0z"
					/>
				</svg>
			</div>
		</nav>
	)
}
