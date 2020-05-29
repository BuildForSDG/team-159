<template>
  <main>
    <div class="w-full banner"
         style="height: 650px; max-height: 650px; min-height: 650px; position: relative;
       overflow: hidden; background-repeat: no-repeat; background-size: cover; z-index: 1;
       background-color: rgb(51, 19, 159);" :style="bgImage">
      <div class="max-w-screen-xl mx-auto">
        <div class="block pt-32 lg:w-full">
          <div class="lg:w-3/4 m-auto">
            <p class="text-lg font-semibold text-white pt-10 text-center text-3xl"><span
              style="color: rgb(0, 255, 85);">Money Lending </span> made Easy</p>

            <p
              class="text-left leading-7 text-white pt-8 lg:w-1/2 m-auto text-lg pb-16 text-center">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur corporis debitis
              dicta error esse mollitia, reprehenderit voluptate. Expedita libero, vero?</p>

            <div class="align-center text-center justify-content-center">
              <router-link
                to="/login"
                class="inline-block shadow text-lg px-24 py-5 leading-none border
              rounded-full text-white hover:border-transparent mt-4 lg:mt-0 focus:shadow-outline
              transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-105"
                style="background-color: rgb(40, 178, 86); border: none;">Start Now
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Capture/>
  </main>
</template>

<script>
import Capture from '../components/Home/Capture.vue';

export default {
  name: 'Home',
  components: {
    Capture,
  },
  data() {
    return {
      bgImage: "background-image: url('https://images.unsplash.com/photo-1454779132693-e5cd0a216"
        + 'ed3?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;'
        + "fit=crop&amp;w=751&amp;q=80');",
    };
  },
};
</script>
