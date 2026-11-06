"use client"
import {useEffect, useState} from "react"
import {socket} from "@/lib/socket"

export default function Inbox(){
	const [menu, setmenu] = useState([])
	const [inbox, setinbox] = useState([])
	const [option, setoption] = useState([])

	useEffect(()=>{
		const fetchdata = async ()=>{
			try {
				socket.connect()
				socket.on("menu", (data)=>{setMenu(data)})
				
			} catch(error){
				console.log(error)
			}
		}
	})

	return (<div className="pt-50 p-20 flex gap-4 bg-[#FFF8E7] h-screen">
		<div className="w-1/3 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5">meanu</div>
		<div className="flex-1 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5">inbox</div>
		<div className="w-1/3 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5">more</div>
	</div>)
}
