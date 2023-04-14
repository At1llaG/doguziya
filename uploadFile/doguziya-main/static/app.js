class Chatbox {








    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
        
    }
    



    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }


    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "Sam", message: r.answer, id_value: r.id_value};
            this.messages.push(msg2);
            
            textField.value = ''
  
  
  
  
            if (r.id_value == 27) {
            
            
          const feedbackMessage = 'Dilerseniz Ağız ve Diş Hastalıkları randevusu için tıklayabilirsiniz:';
          const doctorButton = '<a href="https://www.hastanemyanimda.com/birim/agiz-ve-dis-hastaliklari/" target="_blank"><button type="button" class="btn btn-success">Doktorlar</button></a>';
           
            
        
console.log('test');


fetch('/doctors.json')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error))

    
console.log('test');





  
  
  
  
 
    
    
  const doctors = [
    {

      name: 'Dr. Fulya Tadık Gümüşel',
      imgUrl: 'https://www.hastanemyanimda.com/storage/hastanemyanimda/profiles/dr-fulya-tadik-gumusel.jpeg',
      link: 'https://www.hastanemyanimda.com/doktor/dr-fulya-tadik-gumusel',
    },
    {
      name: 'Dr. Ömer Öner',
      imgUrl: 'https://www.hastanemyanimda.com/storage/hastanemyanimda/profiles-150x150/dr-omer-oner.jpeg?1561521193',
      link: 'https://www.hastanemyanimda.com/doktor/dr-omer-oner',
    },
    {
      name: 'Dr. Güray Gümüşel',
      imgUrl: 'https://www.hastanemyanimda.com/storage/hastanemyanimda/profiles-150x150/dr-guray-gumusel.jpeg?1606005350',
      link: 'https://www.hastanemyanimda.com/doktor/dr-guray-gumusel',
    },
  ];


  
  const doctorButtons = doctors.map(doctor => {
    return `
      <div class="button-container">
          <div class="button">
            <div class="text-container">
              <p>${doctor.name}</p>
            </div>
          </div>
      </div>
    `;
  }).join('');
  
  const feedbackButtons = `
    <div class="feedback-buttons">
      ${doctorButton}
      ${doctorButtons}
    </div>
  `;
  
  const message = { name: 'Sam', message: feedbackMessage + feedbackButtons };
  this.messages.push(message);
}


            
this.updateChatText(chatbox);
            

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam")
            {
                html += '<div class="messages_item messages_item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages_item messages_item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();