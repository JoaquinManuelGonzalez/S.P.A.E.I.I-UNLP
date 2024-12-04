<template>
  <div>
    <!-- Primera Sección: Imagen a la derecha, Título y texto a la izquierda -->
    <section class="flex flex-col md:flex-row items-center py-16 px-4">
      <!-- Apartado de texto a la izquierda -->
      <div class="md:w-1/2 mb-8 md:mb-0 text-center md:text-left">
        <!-- Título con color personalizado -->
        <h2 class="text-5xl font-bold mb-3" style="color: #25535e">
          {{ $t("contenidoLandingPage.relacionesInternacionales.titulo") }}
        </h2>
        <p class="text-lg text-gray-600 dark:text-gray-600">
          {{ $t("contenidoLandingPage.relacionesInternacionales.parrafoUno") }} <br>
          {{ $t("contenidoLandingPage.relacionesInternacionales.inicioParrafoDos") }} <strong style="color: #25535e">{{ $t("contenidoLandingPage.relacionesInternacionales.pri") }}</strong>{{ $t("contenidoLandingPage.relacionesInternacionales.parrafoDos") }}
        </p>
      </div>
      <!-- Imagen a la derecha -->
      <div class="md:w-1/2">
        <img src="../assets/estudiantes-landing-page.jpg" alt="Imagen descriptiva"
          class="w-full h-auto object-cover rounded-lg shadow-lg" />
      </div>
    </section>

    <!-- Segunda Sección: Carrusel de Cards con Flowbite -->
    <section class="py-16 px-4" style="background-color: #96ba3a">
      <h3 class="text-5xl mb-4 font-bold text-center text-white">
        {{ $t("contenidoLandingPage.nuestrasFacultades") }}
      </h3>
      <div class="container mx-auto py-8">
        <CardCarousel :cards="cards" />
      </div>
    </section>
  </div>
</template>

<script>
import CardCarousel from '../components/CardCarousel.vue';
import fau_image from '../assets/logo-fau.png';
import artes_image from '../assets/logo-arte.jpg';
import agraria_image from '../assets/logo-agraria.png';
import astronomica_image from '../assets/logo-astronomica.png';
import economicas_image from '../assets/logo-economicas.png';
import exactas_image from '../assets/logo-exactas.jpg';
import juridicas_image from '../assets/logo-juridica.jpg';
import medicina_image from '../assets/logo-medicina.png';
import naturales_image from '../assets/logo-naturales.png';
import veterinaria_image from '../assets/logo-veterinaria.png';
import humanidades_image from '../assets/logo-humanidades.png';
import informatica_image from '../assets/logo-informatica.png';
import ingenieria_image from '../assets/logo-ingenieria.png';
import odontologia_image from '../assets/logo-odontologia.png';
import periodismo_image from '../assets/logo-periodismo.png';
import psicologia_image from '../assets/logo-psicologia.png';
import social_image from '../assets/logo-trabajo-social.jpg';

export default {
  components: {
    CardCarousel
  },
  computed: {
    cards() {
      return [
        {
          title: this.$t("contenidoLandingPage.cards.fau.title"),
          description: this.$t("contenidoLandingPage.cards.fau.descripcion"),
          contactPhone: '(0221)423-6587/90',
          contactEmail: 'decanato@fau.unlp.edu.ar',
          link: 'https://www.fau.unlp.edu.ar',
          image: fau_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.artes.title"),
          description: this.$t("contenidoLandingPage.cards.artes.descripcion"),
          contactPhone: '(0221) 423-6598 // 423-5756',
          contactEmail: 'academica@fba.unlp.edu.ar',
          link: 'https://fba.unlp.edu.ar/?_gl=1%2Ah4p48c%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: artes_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasAgrarias.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasAgrarias.descripcion"),
          contactPhone: '(0221) 423-6758',
          contactEmail: 'decano@agro.unlp.edu.ar',
          link: 'https://www.agro.unlp.edu.ar/?_gl=1*1fupplp*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: agraria_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasAstronomicas.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasAstronomicas.descripcion"),
          contactPhone: '(0221) 4236593/4236759/4236594/4236592',
          contactEmail: 'extension@fcaglp.unlp.edu.ar',
          link: 'https://www.fcaglp.unlp.edu.ar/?_gl=1%2Aqha31o%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: astronomica_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasEconomicas.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasEconomicas.descripcion"),
          contactPhone: '(0221) 423-6769/71/72',
          contactEmail: 'decanato@econo.unlp.edu.ar',
          link: 'https://www.econo.unlp.edu.ar/?_gl=1*var5zz*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: economicas_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasExactas.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasExactas.descripcion"),
          contactPhone: '(0221) 422-6977/6979/6981',
          contactEmail: 'academic@decanato.exactas.unlp.edu.ar',
          link: 'https://www.exactas.unlp.edu.ar/?_gl=1*5tezet*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: exactas_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasJuridicas.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasJuridicas.descripcion"),
          contactPhone: '(221) 644-2070/644-2090',
          contactEmail: 'decanato@jursoc.unlp.edu.ar',
          link: 'https://www.jursoc.unlp.edu.ar/?_gl=1*rri028*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: juridicas_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasMedicas.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasMedicas.descripcion"),
          contactPhone: '(0221) 424-1596/424-3068/424-2711/423-6711',
          contactEmail: 'alumnado@med.unlp.edu.ar',
          link: 'https://www.med.unlp.edu.ar/?_gl=1*rri028*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: medicina_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasNaturales.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasNaturales.descripcion"),
          contactPhone: '(0221) 423-6773/ 425-8252/ 423-2734',
          contactEmail: 'fcnym@museo.fcnym.unlp.edu.ar',
          link: 'https://www.fcnym.unlp.edu.ar/?_gl=1%2A1mq7hjc%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: naturales_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.cienciasVeterinarias.title"),
          description: this.$t("contenidoLandingPage.cards.cienciasVeterinarias.descripcion"),
          contactPhone: '(0221) 423-6663/ 423-6664/ 424-7642',
          contactEmail: 'prensaydifusion@fcv.unlp.edu.ar',
          link: 'https://www.fcv.unlp.edu.ar/?_gl=1%2A7qa7ng%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: veterinaria_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.humanidades.title"),
          description: this.$t("contenidoLandingPage.cards.humanidades.descripcion"),
          contactPhone: '4230128/4236669/4230125/4236673',
          contactEmail: 'sae@fahce.unlp.edu.ar',
          link: 'https://www.fahce.unlp.edu.ar/?_gl=1*1xxjz3v*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: humanidades_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.informatica.title"),
          description: this.$t("contenidoLandingPage.cards.informatica.descripcion"),
          contactPhone: '(0221) 4277270',
          contactEmail: 'difusion@info.unlp.edu.ar',
          link: 'https://www.info.unlp.edu.ar/?_gl=1%2A16864dd%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: informatica_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.ingenieria.title"),
          description: this.$t("contenidoLandingPage.cards.ingenieria.descripcion"),
          contactPhone: '(0221) 425-8911/ 423-6676',
          contactEmail: 'secretaria.academica@ing.unlp.edu.ar',
          link: 'https://ing.unlp.edu.ar/?_gl=1%2Aekd3v3%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: ingenieria_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.odontologia.title"),
          description: this.$t("contenidoLandingPage.cards.odontologia.descripcion"),
          contactPhone: '(0221) 423-6775',
          contactEmail: 'decanato@folp.unlp.edu.ar',
          link: 'https://www.folp.unlp.edu.ar/?_gl=1*m9rrpx*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: odontologia_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.periodismo.title"),
          description: this.$t("contenidoLandingPage.cards.periodismo.descripcion"),
          contactPhone: this.$t("contenidoLandingPage.cards.periodismo.telefonos"),
          contactEmail: 'decanato@perio.unlp.edu.ar',
          link: 'https://perio.unlp.edu.ar/',
          image: periodismo_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.psicologia.title"),
          description: this.$t("contenidoLandingPage.cards.psicologia.descripcion"),
          contactPhone: '482-4415/482-5931/482-8457',
          contactEmail: 'decanato@psico.unlp.edu.ar',
          link: 'https://www.psico.unlp.edu.ar/?_gl=1*j18lp6*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: psicologia_image
        },
        {
          title: this.$t("contenidoLandingPage.cards.trabajoSocial.title"),
          description: this.$t("contenidoLandingPage.cards.trabajoSocial.descripcion"),
          contactPhone: '(0221)452-5317',
          contactEmail: 'comunicacioninstitucional@trabajosocial.unlp.edu.ar',
          link: 'https://www.trabajosocial.unlp.edu.ar/?_gl=1*1m918fy*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: social_image
        }
      ];
    }
  }
};
</script>
