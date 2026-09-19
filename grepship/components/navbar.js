"use client"
import Link from "next/link"
import {useState, useEffect} from "react"
export default function Navbar(){

	const [profilepic, setprofilepic] = useState("/default_profile.png")
	const [login, setlogin] = useState(true)
	useEffect(()=>{
		async function loadSession(){
			try {
				const res = await fetch("/api/auth/me")
				const data = await res.json()

				if (!data.user)	{
					return
				}
				setlogin(true)
				setprofilepic(data.user.profilepic)
			} catch (err){
				console.log(err)
			}
		}
		loadSession()
	}, [])

	return (
		<nav className="flex fixed top-0 left-0 right-0 h-30  bg-[#26351F] color-[#FFF8E7]">
			<div className="items-center h-full w-1/5 flex">
				<a className="hover-scale-105 flex text-center w-full justify-center h-full">
					<img src="/logo.png" className="h-full p-3"/>
				</a>
			</div>
			<div className="flex items-center justify-center flex-1">
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
			{login ? (
				<div className="w-1/5 h-full flex justify-between items-cneter p-10 h-full">
					<Link href="/">
						<button className="bg-[#e6a82e] text-[#26351f] hover:bg-[#f0b83d] px-4 p-2 rounded-xl cursor-pointer">Inbox</button>
					</Link>
					<div className="w-15 h-full rounded-lg flex items-center bg-[#022520]">
						<div className="rounded-full"><img className="rounded-full w-9 ml-1" src={profilepic} /></div>
					</div>
				</div>
			) : (
				<div className="w-1/5 flex justify-between items-center p-10">
					<Link href="/login"><button className="bg-[#FFF8E7] text-[#26351F] hover:bg-[#E8F0D8] p-2 rounded-xl cursor-pointer">Log In</button></Link>
					<Link href="/signup"><button className="bg-[#E6A82E] text-[#26351F] hover:bg-[#F0B83D] p-2 rounded-xl cursor-pointer">Sign Up</button></Link>
				</div>
			)}
		</nav>
	)
}
