<template>
    <div class="relative w-full max-w-6xl mx-auto">
      <!-- Carousel Wrapper -->
      <div class="overflow-hidden">
        <div
          class="flex transition-transform duration-500 ease-in-out"
          :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
        >
          <!-- Carousel Slides -->
          <div
            v-for="(card, index) in cards"
            :key="index"
            class="flex-none w-full p-4"
          >
            <!-- Card -->
            <div class="card bg-white border rounded-lg shadow-lg flex flex-col md:flex-row">
              <!-- Left Side: Text Content -->
              <div class="w-full md:w-1/2 p-6 flex flex-col justify-center">
                <h2 class="text-xl md:text-2xl font-bold mb-4">{{ card.title }}</h2>
                <p class="text-gray-600 mb-4">
                  <span class="font-semibold">Dirección:</span> {{ card.description }}
                </p>
                <p class="text-gray-600 mb-4">
                  <span class="font-semibold">Teléfono de Contacto:</span> {{ card.contactPhone }}
                </p>
                <p class="text-gray-600 mb-4">
                  <span class="font-semibold">Email de Contacto:</span> {{ card.contactEmail }}
                </p>
                <a
                  :href="card.link"
                  class="text-blue-500 hover:underline font-semibold"
                  target="_blank"
                >
                  Leer más
                </a>
              </div>
              <!-- Right Side: Image -->
              <div class="w-full md:w-1/2 p-6 flex justify-center items-center">
                <img
                  :src="card.image"
                  alt="Image"
                  class="card-image w-full h-60 object-contain rounded-lg"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Navigation Buttons -->
      <div class="absolute top-1/2 transform -translate-y-1/2 left-4 z-10">
        <button
          class="bg-gray-800 bg-opacity-50 text-white p-4 rounded-full shadow-lg hover:bg-opacity-75 focus:outline-none focus:ring-2 focus:ring-gray-300"
          @click="prev"
        >
          ❮
        </button>
      </div>
      <div class="absolute top-1/2 transform -translate-y-1/2 right-4 z-10">
        <button
          class="bg-gray-800 bg-opacity-50 text-white p-4 rounded-full shadow-lg hover:bg-opacity-75 focus:outline-none focus:ring-2 focus:ring-gray-300"
          @click="next"
        >
          ❯
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      cards: {
        type: Array,
        required: true,
      },
    },
    mounted() {
      console.log(this.cards);
    },
    data() {
      return {
        currentIndex: 0,
      };
    },
    computed: {
      maxIndex() {
        return this.cards.length;
      },
    },
    methods: {
      prev() {
        this.currentIndex = (this.currentIndex - 1 + this.maxIndex) % this.maxIndex;
      },
      next() {
        this.currentIndex = (this.currentIndex + 1) % this.maxIndex;
      },
    },
  };
  </script>
  
  <style scoped>
  .card {
    display: flex;
    flex-direction: column; /* Por defecto, las tarjetas serán verticales */
    max-height: 100%; /* Permite que la tarjeta crezca según el contenido */
  }
  
  @media (min-width: 768px) {
    .card {
      flex-direction: row; /* Cambia a horizontal en pantallas medianas o más grandes */
      max-height: 20rem; /* Limita la altura en pantallas más grandes */
    }
  }
  
  .card-image {
    width: 100%;
    height: auto; /* Ajusta automáticamente la altura de la imagen */
    object-fit: contain;
    border-radius: 0.5rem;
  }
  </style>
  