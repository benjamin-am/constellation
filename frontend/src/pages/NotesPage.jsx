import "../pages/NotesPage.scss";

//Import Components
import Header from "../components/Header/Header";
import Notes from "../components/Notes/Notes";
import ViewOutput from "../components/ViewOutput/ViewOutput";
import VerticalNavBar from "../components/VerticalNavBar/VerticalNavBar";

function NotesPage() {
    return(
        <>
        <container className="container">
        <VerticalNavBar />
        <Notes />
        <ViewOutput />
        </container>

        </>
    )
}

export default NotesPage;
