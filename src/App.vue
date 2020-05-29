<template>
  <div id="app" class="overflow-auto">
    <div class="w-full fixed lg:z-50 top-0" style="background-color: rgb(51, 19, 159);">
      <header class="max-w-screen-xl mx-auto">

        <nav class="flex items-center justify-between flex-wrap p-4">

          <div class="flex items-center flex-shrink-0 text-white mr-20">
            <a href="/" class="font-bold font-weight-bolder text-xl tracking-wide">M-Uwezo</a>

          </div>

          <div class="flex-grow">
            <router-link
              to="/"
              class="block mt-4 tracking-wide lg:inline-block text-base hover:bg-blue-600 rounded-sm
            hover:shadow py-1 px-5 lg:mt-0 text-white hover:text-white">Home
            </router-link>

            <router-link
              to="/about"
              class="block mt-4 tracking-wide lg:inline-block text-base hover:bg-blue-600 rounded-sm
            hover:shadow py-1 px-5 lg:mt-0 text-white hover:text-white">About
            </router-link>

            <router-link
              to="/services"
              class="block mt-4 tracking-wide lg:inline-block text-base hover:bg-blue-600 rounded-sm
            hover:shadow py-1 px-5 lg:mt-0 text-white hover:text-white">Services
            </router-link>

            <router-link
              to="/contact"
              class="block mt-4 lg:inline-block tracking-wide text-base hover:bg-blue-600 rounded-sm
            hover:shadow py-1 px-5 lg:mt-0 text-white hover:text-white">Contact
            </router-link>
          </div>
          <div class="block lg:hidden xl:hidden">
            <button class="flex items-center px-3 py-2 border rounded text-teal-200 hover:text-white
          hover:border-white">
              <svg class="fill-current h-3 w-3" viewBox="0 0 20 20"
                   xmlns="http://www.w3.org/2000/svg">
                <title>Menu</title>
                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"></path>
              </svg>
            </button>
          </div>

          <div class="flex justify-center">
            <router-link
              to="/login"
              class="inline-block shadow-md text-base px-6 py-2 leading-none
            border rounded-full text-white hover:border-transparent mt-4 lg:mt-0 hover:shadow-none
            focus:shadow-outline transition duration-500 ease-in-out transform hover:-translate-y-1
            hover:scale-105" style="background-color: rgb(40, 178, 86); border: none;">Sign In
            </router-link>
            <div class="my-auto">
              <i
                class="fab opacity-75 flex-1 cursor-pointer text-lg mr-5 ml-5
              text-white fa-facebook hover:opacity-100"
                aria-hidden="true"></i>
              <i
                class="fab opacity-75 flex-1 text-lg cursor-pointer
              text-white fa-twitter hover:opacity-100"
                aria-hidden="true"></i>
              <i
                class="fab opacity-75 flex-1 text-lg cursor-pointer mr-5 ml-5
              text-white fa-instagram hover:opacity-100"
                aria-hidden="true"></i>
            </div>
          </div>

        </nav>

      </header>
    </div>
    <div class="w-full overflow-auto">
      <router-view/>
    </div>
  </div>
</template>
