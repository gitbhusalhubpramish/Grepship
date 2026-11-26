"use client"
import {useSearchParams} from "next/navigation"
import {useState, useEffect} from "react"

export default function Search(){
	const searchParams= useSearchParams()

	const [users, setusers] = useState(null)

	const query = searchParams.get("q") || ""
	useEffect(()=>{
		if (!query) return
		async function fetchdata(){
			const res = await fetch(`/api/search/search?q=${query}`)
			const data = await res.json()
			console.log(data)
			if (data.users.length!==0){
				setusers(data.users)
			}else{
				setusers(null)
			}
		}
		fetchdata()
		
	}, [query])
	return (
		<div className="pt-30 h-screen w-screen bg-[#fff8e7]">
			{users!==null ? users.map((user, index)=>(<div key={index}>{user.username}</div>)) : (<div className="text-3xl text-center w-full h-full flex justify-center items-center">No result found</div>)}
		</div>
	)
}
