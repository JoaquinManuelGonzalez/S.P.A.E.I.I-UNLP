<template>
    <footer class="shadow dark:bg-gray-900" :style="{ backgroundColor: '#25535E' }">
        <div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
            <div class="sm:flex sm:items-center sm:justify-between space-y-4 sm:space-y-0">
                <!-- Logo y título -->
                <a 
                    href="https://unlp.edu.ar/" 
                    class="flex flex-col sm:flex-row items-center text-center sm:text-left mb-4 sm:mb-0 space-y-2 sm:space-y-0 sm:space-x-3 rtl:space-x-reverse"
                >
                    <img src="../assets/logo-unlp.png" class="h-10" alt="Universidad de La Plata Logo" />
                    <span class="self-center text-xl sm:text-2xl font-semibold text-white">
                        Prosecretaría de Relaciones Internacionales - Universidad Nacional de La Plata
                    </span>
                </a>
                <!-- Lista de enlaces -->
                <ul class="flex flex-wrap justify-center sm:justify-end items-center space-x-6 text-sm font-medium text-gray-500 dark:text-gray-400">
                    <li>
                        <a href="https://unlp.edu.ar/institucional/secretaria_relaciones_institucionales/relaciones-internacionales/prosecretaria_de_relaciones_internacionales_universitarias-14-5014/"
                            class="hover:underline">Sobre nosotros</a>
                    </li>
                    <li>
                        <a href="https://www.instagram.com/internacionalesunlp/"
                            class="text-blue-300 hover:text-violet-400 flex justify-center">
                            <InstagramIcon />
                        </a>
                    </li>
                    <li>
                        <a href="https://www.facebook.com/unlp.edu"
                            class="text-blue-300 hover:text-violet-400 flex justify-center">
                            <FacebookIcon />
                        </a>
                    </li>
                    <li>
                        <a href="https://x.com/unlp"
                            class="text-blue-300 hover:text-violet-400 flex justify-center">
                            <TwitterIcon />
                        </a>
                    </li>
                </ul>
            </div>
            <!-- Divider -->
            <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
            <!-- Texto del footer -->
            <span class="block text-sm text-gray-500 text-center dark:text-gray-400">
                Universidad Nacional de La Plata Av. 7 N° 776, La Plata (CP 1900), Buenos Aires, Argentina. <br>
                Los materiales del Portal Universidad Nacional de La Plata, salvo expresa aclaración, se comparten bajo una Licencia Creative Commons Atribución 2.5.
            </span>
        </div>
    </footer>
</template>

<script>
import InstagramIcon from './icons/InstagramIcon.vue'
import FacebookIcon from './icons/FacebookIcon.vue'
import TwitterIcon from './icons/TwitterIcon.vue'

export default {
    name: 'Footer',
    components: {
        InstagramIcon,
        FacebookIcon,
        TwitterIcon,
    }
}
</script>
