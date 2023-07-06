import { useEffect, useState } from "react";
import { CommentsInterface } from "../interfaces/complaintInterface";
import { baseUrl } from "../components/home";
import axios from "axios";
import { Authentication } from "../interfaces/user";

export const useGetComments = ():CommentsInterface[] =>{
const [comments, setComments] = useState<CommentsInterface[]>([])


useEffect(() => {
    axios.get(`${baseUrl}comments`, {
        auth: (JSON.parse(localStorage.getItem('user')!) as Authentication).auth
    }).then(
        res => {
            console.log(res.data);
            setComments(res.data as CommentsInterface[])
            // console.log(allComplaints, "allComplaints");
        }
    ).catch(
        error => {
            console.log(error, "allcomplaints error");
        })
}, [])

return comments

}
