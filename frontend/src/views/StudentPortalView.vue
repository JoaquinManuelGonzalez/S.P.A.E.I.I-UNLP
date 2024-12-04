<template>
  <div class="h-screen flex">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Área de contenido principal -->
    <div class="flex-1 p-4 md:p-10 overflow-y-auto">
      <!-- Título principal con línea -->
      <h1 class="text-3xl font-bold mb-4">Portal para Alumnos Entrantes</h1>
      <hr class="border-gray-300 mb-4" />

      <!-- Leyenda descriptiva -->
      <p class="text-lg text-gray-700 mb-6">
        En este portal podrás gestionar diversas actividades como la
        repostulación para nuevos períodos de inscripción, la elección de las
        asignaturas que te gustaría cursar dentro de nuestra universidad y la
        consulta de toda la documentación relevante a tus Postulaciones. Navega
        por las opciones en el menú lateral para explorar las diferentes
        funcionalidades.
      </p>

      <!-- Imagen descriptiva -->
      <img
        :src="alumnosInternacionalesImage"
        alt="Alumnos Internacionales en la Universidad Nacional de La Plata"
        class="w-full max-w-3xl mx-auto h-auto rounded-lg shadow-lg"
      />
    </div>
  </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue";
import alumnosInternacionalesImage from "@/assets/estudiantes.webp";

export default {
  name: "Dashboard",
  components: {
    Sidebar,
  },
  data() {
    return {
      alumnosInternacionalesImage,
    };
  },
};
</script>

<style scoped>
/* Aseguramos que el contenedor principal ocupe toda la altura */
h-screen {
  height: 100vh;
}

.flex {
  display: flex;
}

.flex-1 {
  flex: 1;
}

.overflow-y-auto {
  overflow-y: auto; /* Añadido para habilitar el scroll cuando el contenido sobrepase la pantalla */
}
</style>
