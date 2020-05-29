<template>
  <div class="max-w-screen-xl mx-auto">
    <div class="flex-col justify-center align-center py-10">
      <p class="font-bold lg:text-2xl text-center text-black">Grow your business today</p>
      <p
        class="font-semibold text-gray-500 lg:text-sm text-center text-black">
        M-uwezo help you find fund for your growing business</p>
    </div>
    <div class="p-10 flex pt-40">
      <div class="flex-1">
      <div
        class="mx-4 shadow-lg w-3/4 m-auto border rounded-lg  bg-white overflow-hidden
            cursor-pointer hover:border-blue-200 border-transparent hover:border">
        <img :src="research" class="object-cover w-full"
             alt="grow your business">
        <h3 class="text-black py-2 px-5 text-left text-lg font-bold">Grow you business</h3>
        <p class="leading-6 text-black text-left pt-4 px-5 pb-10">Lorem ipsum dolor sit amet,
          consectetur adipisicing elit. Adipisci asperiores error neque sed voluptate. Eligendi
          facere molestias non reiciendis sapiente?</p></div>
    </div>
      <div class="flex-1">
      <div
        class="mx-4 shadow-lg w-3/4 m-auto border rounded-lg bg-white overflow-hidden
            -mt-32 mb-32 cursor-pointer hover:border-blue-200 border-transparent hover:border">
        <img :src="investment" class="object-cover w-full"
             alt="grow your business">
        <h3 class="text-black py-2 px-5 text-left text-lg font-bold">Expand your business</h3>
        <p class="leading-6 text-black text-left pt-4 px-5 pb-10">Lorem ipsum dolor sit amet,
          consectetur adipisicing elit. Adipisci asperiores error neque sed voluptate. Eligendi
          facere molestias non reiciendis sapiente?</p></div>
    </div>
      <div class="flex-1">
      <div
        class="mx-4 shadow-lg  border w-3/4 m-auto rounded-lg  bg-white overflow-hidden
        cursor-pointer hover:border-blue-200 border-transparent hover:border">
        <img :src="invest" class="object-cover w-full"
             alt="grow your business">
        <h3 class="text-black py-2 px-5 text-left text-lg font-bold">Invest more</h3>
        <p class="leading-6 text-black text-left pt-4 px-5 pb-10">Lorem ipsum dolor sit amet,
          consectetur adipisicing elit. Adipisci asperiores error neque sed voluptate. Eligendi
          facere molestias non reiciendis sapiente?</p></div>
    </div>
    </div>
  </div>
</template>

<script>
import invest from '../../assets/invest.svg';
import investment from '../../assets/investment.svg';
import research from '../../assets/researching.svg';

export default {
  name: 'Capture',
  data() {
    return {
      invest,
      investment,
      research,
    };
  },
};
</script>

<style scoped>

</style>
