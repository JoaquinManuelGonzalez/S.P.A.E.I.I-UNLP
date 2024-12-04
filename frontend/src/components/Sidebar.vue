<template>
  <div class="h-screen flex flex-col md:flex-row relative">
    <!-- Fondo difuminado cuando la sidebar está abierta -->
    <div 
      v-if="isSidebarOpen" 
      class="fixed inset-1 bg-black bg-opacity-50 z-40 md:hidden" 
      @click="toggleSidebar"
    ></div>

    <!-- Sidebar -->
    <div
      :class="[
        'fixed inset-y-0 left-0 w-64 bg-gray-200 text-gray-800 shadow-2xl z-50 transition-transform transform',
        isSidebarOpen ? 'translate-x-0' : '-translate-x-full',
        'md:translate-x-0 md:relative md:block'
      ]"
    >
      <!-- Título de la Sidebar -->
      <div class="p-5 text-xl font-semibold bg-gray-200 text-gray-800">
        Menú de Navegación
      </div>

      <!-- Menú de navegación -->
      <nav class="mt-5 space-y-2">
        <ul>
          <li>
            <router-link
              to="/repostulacion"
              class="block py-3 px-5 hover:bg-gray-700 hover:text-white rounded-md transition"
              :class="{ 'border-b-2 border-white': $route.path === '/repostulacion' }"
            >
              Repostulación
            </router-link>
          </li>
          <li>
            <router-link
              to="/eleccion-asignaturas"
              class="block py-3 px-5 hover:bg-gray-700 hover:text-white rounded-md transition"
              :class="{ 'border-b-2 border-white': $route.path === '/eleccion-asignaturas' }"
            >
              Elección de Asignaturas
            </router-link>
          </li>
          <li>
            <router-link
              to="/ver-documentacion"
              class="block py-3 px-5 hover:bg-gray-700 hover:text-white rounded-md transition"
              :class="{ 'border-b-2 border-white': $route.path === '/ver-documentacion' }"
            >
              Ver Documentación
            </router-link>
          </li>
        </ul>
      </nav>

      <!-- Botón para cerrar la sidebar -->
      <div v-if="isSidebarOpen" class="mt-auto p-4 md:hidden">
        <button
          @click="toggleSidebar"
          class="block w-full py-3 text-gray-800 font-semibold hover:bg-gray-700 hover:text-white rounded-md transition"
        >
          Cerrar Menú
        </button>
      </div>
    </div>

    <!-- Botón para abrir la sidebar en pantallas pequeñas -->
    <div
      v-if="!isSidebarOpen"
      @click="toggleSidebar"
      class="md:hidden p-3 text-gray-800 cursor-pointer fixed top-4 left-4 z-30 bg-gray-200 rounded-full shadow-md"
    >
      <span class="block w-auto h-8 text-center font-semibold text-gray-700">
        Abrir Menú
      </span>
    </div>

    <!-- Área de contenido principal -->
    <div class="flex-1 p-4 md:p-10 overflow-y-auto">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      isSidebarOpen: false, // Estado de la sidebar
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
  },
};
</script>

<style scoped>
/* Transición para la sidebar */
.transition-transform {
  transition: transform 0.3s ease-in-out;
}
</style>
