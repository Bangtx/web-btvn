<template>
  <body class="container">
      <header>
          <div class="crossbar-header">
              <div class="waffle-header">
                  <a href="#"><button class="ts-waffle-button"><i class="fas fa-bars"></i></button></a>
                  <span>Anh Nguyen</span>
              </div>
              <div class="search">
                  <i class="fas fa-search"></i>
                  <input type="text" placeholder="Search">
              </div>
              <div class="powerbar-profile">
                  <a href="#"><p class="powerbar"><i class="fas fa-ellipsis-h"></i></p></a>
                  <a href="#"><button><img class="profile" src="image/profile.jpg" alt="profile"></button></a>
              </div>
          </div>
      </header>
      <section class="body">
          <div class="menu">
              <a href="#"><button><i class="far fa-list-alt"></i><br>Question Bank</button></a>
              <a href="#"><button><i class="fas fa-comment-dots"></i><br>Chat</button></a>
              <a href="#"><button><i class="fas fa-users"></i><br>Group</button></a>
              <a href="#"><button><i class="fas fa-phone-alt"></i><br>Call</button></a>
              <a href="#"><button><i class="fas fa-tv"></i><br>Stream</button></a>
              <a href="#"><button><i class="far fa-file"></i><br>Foler</button></a>
              <a href="#"><button><i class="fas fa-ellipsis-h"></i></button></a>
              <a href="#"><button style=" margin-top: 16vh;"><i class="fab fa-buromobelexperte"></i><br>App</button></a>
              <a href="#"><button><i class="far fa-question-circle"></i><br>Help</button></a>
          </div>
          <div class="list">
              <div class="topic">
                  <div><span>Topic:</span></div>
                  <select>
                      <option>A</option>
                      <option>B</option>
                      <option>C</option>
                  </select>
              </div>
              <div class="type">
                  <div>Type:</div>
                  <select>
                      <option>Multiple-C</option>
                      <option>a</option>
                      <option>b</option>
                  </select>
              </div>
              <div class="level">
                  <div>Level:</div>
                  <select>
                      <option>Easy</option>
                      <option>Medium</option>
                      <option>Hard</option>
                  </select>
              </div>
              <div class="doc">
                  <div>Doc:</div>
                  <select>
                      <option>Tài liệu 1</option>
                      <option>Tài liệu 2</option>
                      <option>Tài liệu 3</option>
                  </select>
              </div>
              <QuestionBank/>
          </div>
          <div class="Image">
              <img id="myImage" src="image/laptop.jpg">
          </div>
      </section>
</body>
</template>

<script lang="ts">
import { defineComponent, ref } from '@vue/composition-api'
import axios from 'axios'
import QuestionBank from "@/components/questionBank.vue";
export default defineComponent({
  name: 'Base',
  components: {QuestionBank},
  setup() {
    const getdata = () => {
      axios
      .get('http://127.0.0.1:8000/data/')
      .then(response => (console.log(response.data)))
    }
    getdata()
    return {
      getdata
    }
  }
})
</script>

<style>

</style>