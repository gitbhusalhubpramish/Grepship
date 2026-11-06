"use client"
import {useEffect, useState} from "react"
import {socket} from "@/lib/socket"

export default function Inbox(){
	const [menu, setmenu] = useState([])
	const [inbox, setinbox] = useState([])
	const [option, setoption] = useState([])
	const [chat, setchat] = useState(null)
	const [showoption, setshowoption] = useState(false)

	useEffect(()=>{
		const fetchdata = async ()=>{
			try {
				const res = await fetch("/api/inbox/menu")
				if (!res.ok){
					console.log(res)
					return 
				}
				const data = await res.json()
				setmenu(data)
			} catch(error){
				console.log(error)
			}
		}
		fetchdata()
	})
	useEffect(()=>{
		const fetchdata = async ()=>{
			try{
				if (!chat){
					return
				}
				const res = await fetch(`/api/inbox/${chat}`)
				const data = await res.json()
				setinbox(data)
				const opres = await fetch(`/api/profile/${chat}`)
				const opdata = await opres.json()
				setoption(opdata)
			} catch(error){
				console.log(error)
			}
		}
	},[chat])

	const handelnewmsg = (data)=>{
		setinbox(prev=>[...prev, data])
		setmenu(prev=> prev.fomd(item => item.username === data.username) ? [{username:data.username, profilepic:data.profilepic, isunread:true}, ...prev.filter(item=> item.username !==  data.username)]: [{username:data.username, profilepic: data.profilepic, isunread:true}, ...prev])
	}

	useEffect(()=>{
		socket.connect()
		socket.on("new_message", (data)=>handelnewmsg(data))
	}, [])

	return (<div className="pt-50 p-20 flex gap-4 bg-[#FFF8E7] h-screen">
		<div className="w-1/3 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5">meanu</div>
		<div className="flex-1 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5">inbox</div>
		<div className={`w-1/3 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5 ${showoption ? "hidden" : ""}`}>more</div>
	</div>)
}
