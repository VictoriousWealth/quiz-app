import axios from 'axios';

const API = axios.create({
  baseURL: "https://quiz-ai-app-587e3a869ae8.herokuapp.com",
});

export default API;
