<template>
    <Disclosure as="nav" class="bg-gray-200" v-slot="{ open }" style="filter: drop-shadow(0 0 0.25rem black);">
        <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="relative flex h-20 items-center justify-between">
                <div class="flex flex-1 items-center justify-start">
                    <div class="flex flex-shrink-0 items-center">
                        <RouterLink to="/">
                            <img class="h-12 w-auto" src="../assets/logo-unlp.png" alt="Your Company" />
                        </RouterLink>
                    </div>
                </div>
                <div class="absolute inset-y-0 right-0 flex items-center sm:hidden">
                    <!-- Mobile menu button-->
                    <DisclosureButton
                        class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
                        <span class="absolute -inset-0.5" />
                        <span class="sr-only">Open main menu</span>
                        <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
                        <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
                    </DisclosureButton>
                </div>
                <div class="hidden sm:ml-6 sm:block">
                    <div class="flex space-x-4">
                        <RouterLink to="/" class="text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Inicio</RouterLink>
                        <div class="relative" @click="toggleDropdown">
                            <button class="bg-gray-200 text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium flex items-center">
                                Idiomas
                                <DropDownArrow />
                            </button>
                            <div v-if="dropdownOpen" class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1">
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Español</a>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Inglés</a>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Portugués</a>
                            </div>
                        </div>
                        <RouterLink to="/postularme" class="text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Quiero Postularme</RouterLink>
                        <RouterLink to="/iniciar-sesion" class="text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Iniciar Sesión</RouterLink>
                    </div>
                </div>
            </div>
        </div>

        <DisclosurePanel class="sm:hidden">
            <div class="space-y-1 px-2 pb-3 pt-2">
                <RouterLink to="/" class="block text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">Inicio</RouterLink>
                <div class="relative">
                    <DisclosureButton as="button" class="block w-full text-left bg-gray-200 text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">
                        Idiomas
                    </DisclosureButton>
                    <div class="mt-2 space-y-1">
                        <DisclosureButton as="a" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Español</DisclosureButton>
                        <DisclosureButton as="a" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Inglés</DisclosureButton>
                        <DisclosureButton as="a" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Portugués</DisclosureButton>
                    </div>
                </div>
                <DisclosureButton as="a" href="/postularme" class="block text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">Quiero Postularme</DisclosureButton>
                <DisclosureButton as="a" href="/iniciar-sesion" class="block text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">Iniciar Sesión</DisclosureButton>
            </div>
        </DisclosurePanel>
    </Disclosure>
</template>

<script setup>
import { ref } from 'vue'
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'
import DropDownArrow from './icons/DropDownArrow.vue';

const dropdownOpen = ref(false)

function toggleDropdown() {
    dropdownOpen.value = !dropdownOpen.value
}
</script>