import { useEffect, useState } from "react";
import { axios } from "axios";
import "./PastNotes.scss";


function PastNotes() {
    const [myNotes, setMyNotes] = useState([]);

    // useEffect(() => {
    //     const getAllPosts = () => {
    //       axios
    //         .get(`http://localhost:8080/posts/`)
    //         .then((response) => {
    //           setMyPosts(response.data);
    //           console.log(response.data);
    //         })
    //         .catch((error) => console.log(error));
    //     };
    //     getAllPosts();
    //   }, []);

    return(
     <>
        I want to review past notes here
     
     
     </>
    )
}

export default PastNotes;