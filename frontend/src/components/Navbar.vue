<template>
    <Disclosure as="nav" class="bg-gray-200" v-slot="{ open }" style="filter: drop-shadow(0 0 0.25rem black);">
        <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="relative flex h-20 items-center justify-between">
                <div class="flex flex-1 items-center justify-start">
                    <div class="flex flex-shrink-0 items-center">
                        <RouterLink to="/">
                            <img class="h-12 w-auto" src="../assets/logo-unlp.png" alt="Logo Universidad Nacional de La Plata" />
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
                        <RouterLink to="/" class="text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">{{ $t("navBar.itemInicio") }}</RouterLink>
                        <div class="relative" @click="toggleDropdown">
                            <button class="bg-gray-200 text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium flex items-center">
                                {{ $t("navBar.itemIdiomas.idiomas") }}
                                <DropDownArrow />
                            </button>
                            <div v-if="dropdownOpen" class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1">
                                <a @click="$i18n.locale = 'es'" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">{{ $t("navBar.itemIdiomas.opcionEspañol") }}</a>
                                <a @click="$i18n.locale = 'en'" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">{{ $t("navBar.itemIdiomas.opcionIngles") }}</a>
                                <a @click="$i18n.locale = 'pt'" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">{{ $t("navBar.itemIdiomas.opcionPortugues") }}</a>
                            </div>
                        </div>
                        <RouterLink to="/primer-formulario" class="text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">{{ $t("navBar.itemPostularme") }}</RouterLink>
                        <a :href="authUrl" class="text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">{{ $t("navBar.itemIniciarSesion") }}</a>
                    </div>
                </div>
            </div>
        </div>

        <DisclosurePanel class="sm:hidden">
            <div class="space-y-1 px-2 pb-3 pt-2">
                <RouterLink to="/" class="block text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">{{ $t("navBar.itemInicio") }}</RouterLink>
                <div class="relative">
                    <DisclosureButton as="button" class="block w-full text-left bg-gray-200 text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">
                        {{ $t("navBar.itemIdiomas.idiomas") }}
                    </DisclosureButton>
                    <div class="mt-2 space-y-1">
                        <DisclosureButton @click="$i18n.locale = 'es'" as="a" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">{{ $t("navBar.itemIdiomas.opcionEspañol") }}</DisclosureButton>
                        <DisclosureButton @click="$i18n.locale = 'en'" as="a" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">{{ $t("navBar.itemIdiomas.opcionIngles") }}</DisclosureButton>
                        <DisclosureButton @click="$i18n.locale = 'pt'" as="a" href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">{{ $t("navBar.itemIdiomas.opcionPortugues") }}</DisclosureButton>
                    </div>
                </div>
                <DisclosureButton as="a" href="/primer-formulario" class="block text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">{{ $t("navBar.itemPostularme") }}</DisclosureButton>
                <DisclosureButton as="a" :href="authUrl" class="block text-gray-600 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-base font-medium">{{ $t("navBar.itemIniciarSesion") }}</DisclosureButton>
            </div>
        </DisclosurePanel>
    </Disclosure>
</template>

<script setup>
import { ref } from 'vue';
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue';
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline';
import DropDownArrow from './icons/DropDownArrow.vue';

// Variable reactiva para manejar el estado del dropdown
const dropdownOpen = ref(false);

function toggleDropdown() {
  dropdownOpen.value = !dropdownOpen.value;
}

// Acceder a la variable de entorno para la URL base
const apiBaseUrl = import.meta.env.VITE_APP_BASE_URL; // Valor por defecto para desarrollo

// Construir el enlace dinámico
const authUrl = `${apiBaseUrl}/auth`;
</script>

