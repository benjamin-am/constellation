import { useEffect, useState } from "react";
import axios from "axios";
import "./PastNotes.scss";


function PastNotes() {
    const [myNotes, setMyNotes] = useState([]);

    useEffect(() => {
        const getAllPosts = () => {
          axios
            .get(`http://127.0.0.1:8000/api/notes/`)
            .then((response) => {
              setMyNotes(response.data);
              console.log(response.data);
            })
            .catch((error) => console.log(error));
        };
        getAllPosts();
      }, []);

    return(

     <section className="notesDisplay__section">
        {myNotes.length === 0 ? (
            <div className="notesDisplay__textContainer">
            <div className="=notesDisplay__noEntries">
                There are no notes to display.
            </div>
        </div>
        ) : (
            myNotes.map((notes) => (
                <div className="notesDisplay__textContainer" key={notes.created_at}>
                     {/* <p>{notes.created_at}</p> */}
                     <h3>{notes.title}</h3>
                     <p>{notes.content}</p>

                    </div>

            ))
        )}
        
     
     
     </section>
    )
}

export default PastNotes;