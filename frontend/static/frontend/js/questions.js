// Django's csrf_token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie('csrftoken');

// Area to be changed
let header = document.getElementById('heading');
let wrapper = document.getElementById('wrapper');

// MENU buttons
const resourcesButton = document.getElementById('resourcesButton');
const questionsButton = document.getElementById('questionsButton');

resourcesButton.addEventListener('click', () => {
    header.innerHTML = 'Resources';
    wrapper.innerHTML = '';
});

questionsButton.addEventListener('click', () => {
    buildList();
});

buildList();

function buildList() {

    // header.innerHTML = '';
    wrapper.innerHTML = '';

    header.innerHTML = 'Questions';

    const url = 'http://127.0.0.1:8000/api/question-list/';
    fetch(url)
    .then((response) => response.json())
    .then((data) => {
        // console.log(data);
        data.forEach(quiz => {
            const date = new Date(quiz.qs_date_added);
            const options = {
                  day: "numeric",
                  month: "long", //to display the full name of the month
                  year: "numeric"
            }
            quiz.qs_answer = quiz.qs_answer.replaceAll('\n', '<br>')
            async function getUserCaller(id) {
                let user = await getUser(id);
                return user;
            }
            const d = date.toLocaleDateString("en-US", options);

            const user = getUserCaller(quiz.qs_owner);
            // console.log(user)
            let question = `
                    <div class="border rounded border-secondary p-4 pt-1 pb-1 mb-2">
                        <p class=" owner-date m-0 p-0 text-end"><b>added by:</b> ${user.username}   <b>date:</b> ${d}</p>
                        <p><strong><a href="#"  class="text-decoration-none quiz-title">${ quiz.qs_title }</a></strong></p>
                        <small>${quiz.qs_answer}</small>
                    </div>
                    `
            wrapper.innerHTML += question;
        });

        return data;
        
    }).then((data) => {
        questionTitles = document.getElementsByClassName('quiz-title');
        for (let i in data) {
            // const editButton = document.getElementsByClassName(`edit`)[i];
            const questionTitle = document.getElementsByClassName(`quiz-title`)[i];
            
    
            // editButton.addEventListener('click', () => {
            //     editTask(data[i])
            // });
    
            // deleteButton.addEventListener('click', () => {
            //     deleteTask(data[i])
            // });
            // console.log(editButton)
    
            questionTitle.addEventListener('click', () => {
                showQuestionDetail(data[i], header, wrapper);
            });
        }
    })
}

async function getUser(id) {
    try {
        return fetch(`http://127.0.0.1:8000/api/user-detail/${id}`)
        .then(response => response.json())
        .then(response => {return response})
    } catch (error) {
        console.log(error);
    }
}

async function showQuestionDetail(question, header, wrapper) {
    header.innerHTML = `${question.qs_title}`;
    const date = new Date(question.qs_date_added);
    const options = {
            day: "numeric",
            month: "long", //to display the full name of the month
            year: "numeric"
    }
    owner = await getUser(question.qs_owner)
    wrapper.innerHTML = ''
    
    const d = date.toLocaleDateString("en-US", options);
    const details = `
        <div class="border m-3 ms-0 p-3">
        <table class="table table-sm table-bordered border-secondary">
            <tr>
                <th><h5>Attribute</h5></th>
                <th><h5>Details</h5></th>
            </tr>
            <tr>
                <td><b>ID</b></td>
                <td class="text-muted">${ question.id }</td>
            <tr>
            <tr>
                <td><b>Created On</b></td>
                <td class="text-muted">${ d }</td>
            <tr>
                <td><b>Owner</b></td>
                <td class="text-muted">${ owner.username }</td>
                
            </tr>
            <tr>
                <td><b>Question</b></td>
                <td>${ question.qs_title }</td>
            </tr>
            <tr>
                <td><b>Type</b></td>
                <td>${ question.qs_type }</td>
            </tr>
            <tr>
                <td><b>Answer</b></td>
                <td>${ question.qs_answer }</td>
            </tr>
        </table>
        <a href="#">
        <button type="button" id="editQuestionButton" class="btn btn-primary" 
        data-bs-toggle="modal" data-bs-target="#exampleModal">Edit</button></a>
    <a href="#">
        <button type="button" id="deleteQuestionButton" class="btn btn-danger"
        >Delete</button></a>
        </div>

        <!-- edit question Modal -->
        <!-- Modal -->
        <div class="modal" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                ...
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
    `
    wrapper.innerHTML = details;

    // Buttons
    const editQuestionButton = document.getElementById('editQuestionButton');
    

    const deleteQuestionButton = document.getElementById('deleteQuestionButton');
    // const editQuestionModal = document.getElementById('editQuestionModal');

    editQuestionButton.addEventListener('click', () => {
        editQuestion(question);
    });
    deleteQuestionButton.addEventListener('click', () => {
        deleteQuestion(question);
    });
}

function editQuestion(question) {
    console.log('edit', question)
    
}

function deleteQuestion(question) {
    console.log('delete', question)
}

