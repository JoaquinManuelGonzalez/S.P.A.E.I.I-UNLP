<template>
  <div class="h-screen flex flex-col md:flex-row">
    <!-- Sidebar -->
    <div
      :class="[
        'w-64 bg-gray-200 text-gray-600 shadow-lg',
        isSidebarOpen ? 'block' : 'hidden', // Mostrar u ocultar la sidebar en dispositivos pequeños
        'md:block', // Siempre visible en pantallas medianas o más grandes
        'h-full', // Asegura que la sidebar ocupe toda la altura
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
              class="block py-3 px-5 hover:bg-gray-700 hover:text-white hover:border-b-2 hover:border-white rounded-md transition"
              :class="{
                'border-b-2 border-white': $route.path === '/repostulacion',
              }"
            >
              Repostulación
            </router-link>
          </li>
          <li>
            <router-link
              to="/eleccion-asignaturas"
              class="block py-3 px-5 hover:bg-gray-700 hover:text-white hover:border-b-2 hover:border-white rounded-md transition"
              :class="{
                'border-b-2 border-white':
                  $route.path === '/eleccion-asignaturas',
              }"
            >
              Elección de Asignaturas
            </router-link>
          </li>
          <li>
            <router-link
              to="/ver-documentacion"
              class="block py-3 px-5 hover:bg-gray-700 hover:text-white hover:border-b-2 hover:border-white rounded-md transition"
              :class="{
                'border-b-2 border-white': $route.path === '/ver-documentacion',
              }"
            >
              Ver Documentación
            </router-link>
          </li>
        </ul>
      </nav>

      <!-- Botón para cerrar la sidebar (visible solo cuando la sidebar está abierta) -->
      <div v-if="isSidebarOpen" class="mt-auto p-4">
        <button
          @click="toggleSidebar"
          class="block w-full py-3 text-gray-800 font-semibold hover:bg-gray-700 hover:text-white hover:border-b-2 hover:border-white rounded-md transition"
        >
          Cerrar Menú
        </button>
      </div>
    </div>

    <!-- Botón para abrir la sidebar en pantallas pequeñas -->
    <div
      v-if="!isSidebarOpen"
      @click="toggleSidebar"
      class="md:hidden p-3 text-gray-800 cursor-pointer fixed top-16 left-4 z-50 bg-gray-200 rounded-full shadow-md"
    >
      <!-- Texto en lugar del ícono de hamburguesa -->
      <span class="block w-auto h-8 text-center font-semibold text-gray-700">
        Abrir Menú
      </span>
    </div>

    <!-- Área de contenido principal -->
    <div class="flex-1 p-4 md:p-10">
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
/* Estilos personalizados para la transición de la sidebar */
</style>
