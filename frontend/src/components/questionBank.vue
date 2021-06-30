<template>
<div class="list-MSSV">
    <select multiple ="multiple">
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
</template>

<script lang="ts">
import { defineComponent, ref } from '@vue/composition-api'
import axios from 'axios'
export default defineComponent({
  name: 'QuestionBank',
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