import { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../pages/NotesPage.scss";

//Import Components
import Notes from "../components/Notes/Notes";
import ViewOutput from "../components/ViewOutput/ViewOutput";
import VerticalNavBar from "../components/VerticalNavBar/VerticalNavBar";

function NotesPage() {
    const [notesText, setNotesText] = useState("");

    const handleSave = (e) => {
        console.log("successfully saved")
        axios
        .post(`https://d020f81f-06af-4479-bcbc-0be7c8845f8d.mock.pstmn.io`, notesText)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log("error saving post", error);

        });
    }
    
    return(
        <>
        <section className="container">
        <VerticalNavBar onSave={handleSave}/>
        <Notes notesText={notesText} setNotesText={setNotesText} onSave={handleSave}/>
        <ViewOutput notesText={notesText}/>
        </section>

        </>
    )
}

export default NotesPage;
