"use client"
import {useEffect, useState, useRef} from "react"
import {socket} from "@/lib/socket"
import {SendHorizontal} from "lucide-react"

export default function Inbox(){
	const [menu, setmenu] = useState([])
	const [inbox, setinbox] = useState([])
	const [option, setoption] = useState([])
	const [chat, setchat] = useState(null)
	const [showoption, setshowoption] = useState(false)
	const [msg, setmsg] = useState("")
	const chatref = useRef(null)
	
	useEffect(()=>{
		if (!socket.connected){
			socket.disconnect()
			socket.connect()
		}
	})

	useEffect(()=>{
		const fetchdata = async ()=>{
			try {
				const res = await fetch("/api/inbox/menu")
				if (!res.ok){
					console.log("err")
					console.log(res)
					return 
				}
				const data = await res.json()
				console.log("success")
				console.log(data)
				setmenu(data)
			} catch(error){
				console.log(error)
			}
		}
		fetchdata()
	},[])
	useEffect(()=>{
		const fetchdata = async ()=>{
			try{
				if (!chat){
					return
				}
				const res = await fetch(`/api/inbox/${chat}`)
				const data = await res.json()
				setinbox({"message":data.message.message, "profilepic": data.profile_pic.profile_pic})
				console.log(inbox)
				console.log(data)
				const opres = await fetch(`/api/profile/${chat}`)
				const opdata = await opres.json()
				setoption(opdata)
			} catch(error){
				console.log(error)
			}
		}
		fetchdata()
	},[chat])

	const handelnewmsg = (data)=>{
		if (data.username===chat){
			setinbox(prev=>({...prev, message:[...(prev?.message || []), data]}))
		}
		setmenu(prev=> prev.find(item => item.username === data.username) ? [{username:data.username, profilepic:data.profilepic, isunread:true}, ...prev.filter(item=> item.username !==  data.username)]: [{username:data.username, profilepic: data.profilepic, isread:true}, ...prev])
	}

	useEffect(()=>{
		socket.connect()
		socket.on("new_message", (data)=>handelnewmsg(data))
	})
	
	useEffect(()=>{
		if (chatref.current){
			chatref.current.scrollTop = chatref.current.scrollHeight
		}
	}, [inbox])

	const sendmsg = ()=>{
		socket.timeout(5000).emit("send_message", {"message":msg, "reciver": chat, "time": new Date()}, (err, res) => {
				if(err){
					console.log(err)
					alert("API connection error")
				}
				if (res?.status==="success"){
					setinbox((prev)=> ({ ...prev, message:[...(prev?.message || []), {"reciver":chat, "message":msg}]}))
					setmsg("")
				}
			}
		)
	}

	return (<div className="pt-50 p-20 flex gap-4 bg-[#FFF8E7] h-screen">
		<div className="w-1/3 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5">
			{menu ? menu.map(item =>(
				<div onClick={(e)=>setchat(item.username)} className="hover:cursor-pointer rounded-3xl h-14 p-2 flex gap-3 items-center bg-[#FFF1CC] hover:bg-[#FFEBC0] border border-[#E4DFC9] mb-5" key={item.username}>
					<img className="h-10 rounded-full aspect-square" alt="user" src={item.profile_pic}/>
					<p className="overflow-hidden flex-1 font-semibold">{item.username}</p>
					{!item.isread ? <div className="bg-red-700 rounded-full w-2 h-2 mr-5 shrink-0"/> : <></>}
				</div>
			)) : <p className="h-full w-full items-center flex justify-center">No messages sent or recived</p>}
		</div>
		<div className="flex-1 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5">
			{chat!==null ?(
				<div className="flex h-full flex-col">
					<div ref={chatref} className="w-full overflow-y-auto">{inbox?.message?.map((item,index) =>(
						<div key={item._id || index} className={`flex items-center ${item.sender===chat ? "" : "flex-row-reverse"} m-5`}>
							<img src={inbox.profilepic} alt="user" className="h-10 w-10 rounded-full"/>
							<p className={`rounded-xlmax-w-2/3 m-2 bg-[#d3d3ce] rounded-md p-2 ${item.sender===chat? "rounded-bl-none" : "rounded-br-none"}`}>{item.message}</p>
						</div>
					))}
					</div>
				

				<div className="mt-auto w-full flex h-10 bg-[#fff3cc] justify-center items-center rounded-lg focus-within:outline-2 outline-[#dfe3cc]">
					<input type="text" className="w-full bg-[#fff3cc] focus:outline-none focus:ring-0 p-2 pr-12 h-full rounded-lg" placeholder="Write a message" value={msg} onChange={(e)=>setmsg(e.target.value)} onKeyDown={(e)=>{e.key==='Enter'? sendmsg() :null}}/>
					<SendHorizontal color="#025f5f" className="cursor-pointer" onClick={sendmsg}/>
				</div>
				</div>

				) : <p className="flex h-full justify-center items-center">No chat selected</p>
			}
		</div>
		<div className={`w-1/3 bg-[#FFFFFF] h-full border-1 border-[#e4dfc9] rounded-3xl p-5 ${showoption ? "" : "hidden"}`}>more</div>
	</div>)
}
