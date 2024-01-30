DB --> main.db 

Wenn nicht vorhanden --> setup.py

Server start --> main.py laufen lassen

import React, { useState } from 'react';
import LikeMenu from '../../components/UserComponents/Likes/LikeMenu';
import Navibar from '../../components/Navbar';
import './Likes.css'; 
import LikeWindow from '../../components/UserComponents/Likes/LikeWindow';

const Likes = () => {
  const [selectedLike, setSelectedLike] = useState('');

  const handleLikeSelect = (likeId) => {
    setSelectedLike(likeId);
  };

  return (
    <>
      <Navibar />
      <div className="like-app-container">
        <div className="like-mmenu">
          <LikeMenu selectLike={handleLikeSelect} selectedLike={selectedLike} />
        </div>
        <div className="like-window"> 
          <LikeWindow selectedLike={selectedLike} /> 
        </div>
      </div>
    </>
  );
};

export default Likes;


import React, { useState, useEffect } from 'react';
import { getHTTPRequest } from '../../serverPackage';
import { Container, Row, Col, Image, Card, Form, Button } from 'react-bootstrap';
import { Formik, Field, ErrorMessage } from 'formik';

const LikeWindow = ({ selectedLike }) => {

  const [likeContent, setLikeContent] = useState(null);
  let params = [sessionStorage.getItem('userID'),sessionStorage.getItem('selectedLike') ]

    const handleChatLike = () => {
      const AddChat = getHTTPRequest("addChats", params)
      const freeemeee = getHTTPRequest("deleteLike", params)
      setLikeContent(null)
    }
    const handleChatDislike = () => {
      const AddChat = getHTTPRequest("deleteLike", params)
      setLikeContent(null)
    } 

  useEffect(() => {
    const fetchLikeContent = async (likeId) => {
      try {
        if(sessionStorage.getItem('leere') != 0)
        {
        const response = await getHTTPRequest("getCompanyInfos", [likeId]);
        const parsedContent = JSON.parse(response);
        setLikeContent(parsedContent);
        }
        else{
          setLikeContent(null)
        }

      } catch (error) {
        console.error('Error fetching like content:', error);
        setLikeContent(null);
      }
    };


    

    
    const selectedContent = sessionStorage.getItem('selectedLike');
    
    if (selectedContent != null && selectedContent !== (selectedLike +2 ).toString()) {
      fetchLikeContent(selectedContent);
    } else {
      // Reset likeContent when no content is selected
      setLikeContent(null);
    }
  }, [selectedLike]);
  console.log(likeContent)
  return (
    <div className="like-window">
      {likeContent ? (
        <div className='profil-containerl'>
        <Container className="profil-containerl">
          <Row className="justify-content-md-center profil-row">
            <Col md={6} className="profil-col">
              <div className="profil-bild-container">
                <Image src={ "./src/images/" + likeContent[0][8]} roundedCircle className="profil-bild" />
              </div>
              <Form.Group>
                <Form.Control
                  type="text"
                  placeholder={likeContent[0][1]}
                  name={likeContent[0][1]}
                  className="profil-input"
                  readOnly
                />
              </Form.Group>
              <Form.Group>
                <Form.Control
                  type="text"
                  placeholder= {likeContent[0][2]}
                  name="email"
                  className="profil-input"
                  readOnly
                />
              </Form.Group>
              <Form.Group>
                <Form.Control
                  type="text"
                  placeholder= {likeContent[0][3]}
                  name="standort"
                  className="profil-input"
                  readOnly
                />
              </Form.Group>
            </Col>
            <Col md={6}>
              <Card className="profil-card">
                <Card.Body>
                  <Card.Title>Wer wir sind</Card.Title>
                  <Form.Control
                    as="textarea"
                    placeholder={likeContent[0][4]}
                    rows={3}
                    name="beschreibung"
                    className="profil-input"
                    readOnly
                  />
                </Card.Body>
              </Card>
              <Card className="profil-card">
                <Card.Body>
                  <Card.Title>Was wir bieten</Card.Title>
                  <Form.Control
                    as="textarea"
                    placeholder={likeContent[0][5]}
                    rows={3}
                    name="angebote"
                    className="profil-input"
                    readOnly
                  />
                </Card.Body>
              </Card>
              <Card className="profil-card">
                <Card.Body>
                  <Card.Title>Karrierechancen</Card.Title>
                  <Form.Control
                    as="textarea"
                    placeholder= {likeContent[0][6]}
                    rows={3}
                    name="karriere"
                    className="profil-input"
                    readOnly
                  />
                </Card.Body>
              </Card>
              <Card className="profil-card">
                <Card.Body>
                  <Card.Title>Unsere Geschichte</Card.Title>
                  <Form.Control
                    as="textarea"
                    placeholder={likeContent[0][7]}
                    rows={3}
                    name="geschichte"
                    className="profil-input"
                    readOnly
                  />
                </Card.Body>
              </Card>
             
        
            </Col>
            <div style={{ backgroundColor: 'lightgray', height: '100px', width: '100%'}}>
           <div className='d-flex justify-content-center align-items-center'>
              <Button className='round-btn' onClick={handleChatLike}> 
                 </Button>
                <Button variant="danger" className="round-btn" onClick={handleChatDislike}>
                </Button>
                </div>
          </div>
            
          </Row>
          
        </Container>
        
        </div>
      ) : (
        <div className="no-content">
          <p>Kein Like ausgewählt </p>
        </div>
      )}
    </div>
  );
};

export default LikeWindow;



import React, { useState, useEffect } from 'react';
import { getHTTPRequest } from '../../serverPackage';
import LikeWindow from './LikeWindow';


const LikeOptions = ({ selectLike }) => {
  
  const handleLikeSelect = (likeId) => {
    sessionStorage.setItem('selectedLike', likeId)
    selectLike(likeId);
  };

  const [likeItems, setLikeItems] = useState([]);

  const fetchLikesData = async () => {
    const uID = sessionStorage.getItem('userID');
    const response = await getHTTPRequest('getLikes', [uID]);
    if(response == "None")
    {
      sessionStorage.setItem('leere', 0)
    }
    else{
      sessionStorage.setItem('leere', 1)
    }
    const processedLikes = await processLikes(JSON.parse(response));
    console.log(processedLikes)
    setLikeItems(processedLikes);
  };

  const processLikes = async (likesData) => {
    const likeItems = [];
    for (const likeData of likesData) {
      const companyID = likeData;
      const companyName = await fetchCompanyName(companyID);
      const likeItem = {
        id: likeData,
        content: companyName,
      };
      likeItems.push(likeItem);
    }
    return likeItems;
  };

  async function fetchCompanyName(companyID) {
    const response = await getHTTPRequest('getCompanyInfox', [companyID]);
    const companyProfile = JSON.parse(response);
    return companyProfile[0];
  }

  useEffect(() => {
    fetchLikesData();
  }, []);

  const renderLikeOptions =  () => {
    const selectedLikeId = sessionStorage.getItem('selectedLike');
    console.log(selectedLikeId)
    return likeItems.map((likeItem) => (
      <div
        key={likeItem.id}
        className={`like-option ${sessionStorage.getItem('selectedLike') == likeItem.id ? 'active' : ''}`}
        onClick={() => handleLikeSelect(likeItem.id)}
      >
        <div className="like-box">
          <h3>{likeItem.content}</h3>
        </div>
      </div>
    ));
  };

  return (
    <div className="like-menu">
      {renderLikeOptions()}
    </div>
  );
};

export default LikeOptions;


.like-menu {
  height: 100%;
  width: 100%;
  background-color: #f0f0f0cc;
  color: rgba(0, 0, 0, 0.61);
  padding: 15px;
  border-radius: 12px;
  overflow-y: auto;
  overflow-x: hidden;
}

.like-options {
  display: flex;
  flex-direction: column;
}

.like-option {
  margin-bottom: 15px;
}

.like-box {
  border: 1px solid transparent;
  border-radius: 12px;
  padding: 10px;
  width: 100%; 
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s, border-color 0.2s;
  margin-bottom: 10px;
  box-sizing: border-box; 
}

.like-box:hover {
  transform: scale(1.02);
  border-radius: 12px;
}

.like-option.active {
  background-color: #7289da;
  border-radius: 12px;
}

.like-box.active {
  border-color: #0074cc;
}

.like-box h3 {
  margin-top: 0;
  margin-bottom: 5px;
  font-size: 18px;
}

.like-box p {
  margin: 0;
  font-size: 14px;
}



import React, { useState, useEffect } from 'react';
import './ChatMenu.css';
import { getHTTPRequest } from '../../serverPackage';

const ChatMenu = ({ selectChat }) => {
  const [chatItems, setChatItems] = useState([]);
  const [selectedChat, setSelectedChat] = useState(sessionStorage.getItem('selectedChat'));
  const userID = sessionStorage.getItem('userID');

  const fetchChatsData = async () => {
    const uID = sessionStorage.getItem('userID');
    const response = await getHTTPRequest('getChats', [uID]);

    const processedChats = await processChats(JSON.parse(response));
    setChatItems(processedChats);
  };

  const processChats = async (chatsData) => {
    const mappedChats = chatsData.map(async (chatData) => {
      const companyId = chatData;
      const companyName = await fetchCompanyName(chatData[0]);
      return {
        id: chatData[0],
        content: companyName,
        chatid: chatData[1]
      };
    });

    return Promise.all(mappedChats);
  };

  async function fetchCompanyName(companyId) {
    const response = await getHTTPRequest('getCompanyInfox', [companyId]);
    const companyProfile = JSON.parse(response);
    return companyProfile[0][0];
  }

  useEffect(() => {
    fetchChatsData();
  }, []);

  const renderChatOptions = () => {
    return chatItems.map((chatItem) => (
      <div
        key={chatItem.id}
        className={`chat-option ${selectedChat === chatItem.id ? 'active' : ''}`}
        onClick={() => handleChatClick(chatItem.id, chatItem.content, chatItem.chatid)}
      >
        <div className="chat-box">
          <h3>{chatItem.content}</h3>
        </div>
      </div>
    ));
  };

  const handleChatClick = (cId, chatContent, chatid) => {
    sessionStorage.setItem('SelectedCompany', cId);
    sessionStorage.setItem('SelectedChat', chatid);
    console.log(chatid)
    setSelectedChat(cId);
    selectChat(cId, chatContent);
  };

  return <div>{renderChatOptions()}</div>;
};

export default ChatMenu;