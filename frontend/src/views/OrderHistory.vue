<template>
  <div>
    <b-card title="Historial de Órdenes por Paciente" class="mb-4">
      <b-form @submit.prevent="buscarHistorial">
        <b-col>
          <b-col cols="9">
            <b-form-group label="Documento del paciente">
              <b-form-input v-model="documento" required />
            </b-form-group>
          </b-col>
          <b-col cols="3" class="d-flex align-items-center">
            <b-button type="submit" variant="primary" block>Buscar</b-button>
          </b-col>
        </b-col>
      </b-form>

      <b-alert
        v-if="mensaje"
        :variant="mensajeColor"
        class="mt-3"
        dismissible
      >
        {{ mensaje }}
      </b-alert>
    </b-card>

    <b-card v-if="ordenes.length" header="Órdenes encontradas" class="mb-4">
      <b-table :items="ordenes" :fields="fields" hover small responsive>
        <template #cell(fecha_creacion)="row">
          {{ formatearFecha(row.item.fecha_creacion) }}
        </template>
        <template #cell(acciones)="row">
          <b-button
            size="sm"
            variant="info"
            @click="verDetalle(row.item.id)"
          >
            Ver detalle
          </b-button>
        </template>
      </b-table>
    </b-card>

    <b-modal v-model="showModal" title="Detalle de la Orden" hide-footer>
      <div v-if="detalleOrden">
        <b-list-group>
          <b-list-group-item>
            <strong>Número:</strong> {{ detalleOrden.numero_orden }}
          </b-list-group-item>
          <b-list-group-item>
            <strong>Fecha:</strong> {{ formatearFecha(detalleOrden.fecha_creacion) }}
          </b-list-group-item>
          <b-list-group-item>
            <strong>Estado:</strong> {{ detalleOrden.estado }}
          </b-list-group-item>
        </b-list-group>
      </div>
    </b-modal>
  </div>
</template>

<script>
import api from "@/api";

export default {
  data() {
    return {
      documento: "",
      ordenes: [],
      detalleOrden: null,
      mensaje: "",
      mensajeColor: "danger",
      showModal: false,
      fields: [
        { key: "numero_orden", label: "Número de Orden" },
        { key: "fecha_creacion", label: "Fecha de Creación" },
        { key: "estado", label: "Estado" },
        { key: "acciones", label: "Acciones" },
      ],
    };
  },
  methods: {
    async buscarHistorial() {
      this.detalleOrden = null;
      this.ordenes = [];
      this.mensaje = "";
      try {
        const res = await api.get(`/ordenes/paciente/${this.documento}`);
        this.ordenes = res.data;
        this.mensaje = this.ordenes.length
          ? ""
          : "No se encontraron órdenes para este paciente.";
        this.mensajeColor = "warning";
      } catch (error) {
        this.mensaje = "Error al buscar las órdenes del paciente.";
        this.mensajeColor = "danger";
      }
    },
    async verDetalle(idOrden) {
      try {
        const res = await api.get(`/ordenes/${idOrden}`);
        this.detalleOrden = res.data;
        this.showModal = true;
      } catch (error) {
        this.mensaje = "Error al cargar el detalle de la orden.";
        this.mensajeColor = "danger";
      }
    },
    formatearFecha(fecha) {
      return new Date(fecha).toLocaleString("es-CO");
    },
  },
};
</script>
