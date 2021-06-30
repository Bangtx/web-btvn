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
              <div class="list-MSSV">
                  <select multiple size="16">
                      <option>20195793</option>
                      <option>20196281</option>
                      <option>20193214</option>
                      <option>20192464</option>
                      <option>20193464</option>
                      <option>20196523</option>
                      <option>20193254</option>
                      <option>20191324</option>
                      <option>20191444</option>
                      <option>20195342</option>
                      <option>20192461</option>
                      <option>20191253</option>
                      <option>20193153</option>
                      <option>20195315</option>
                      <option>20194123</option>
                      <option>20193412</option>
                      <option>20195231</option>
                      <option>20191341</option>
                      <option>20191244</option>
                      <option>20195232</option>
                      <option>20191241</option>
                      <option>20194865</option>
                      <option>20192167</option>
                  </select>
              </div>
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
export default defineComponent({
  name: 'Base',
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