<template>
    <section class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6"></div>
                <div class="col-sm-6">
                    <ol class="breadcrumb float-sm-right">
                        <button
                            type="button"
                            class="btn btn-default"
                            @click="setDesactiveBatch()"
                        >
                            <li class="breadcrumb-item">Lotes de producción</li>
                        </button>
                    </ol>
                </div>
            </div>
        </div>
        <!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
        <div class="container-fluid">
            <div class="row" v-if="list">
                <div class="col-12">
                    <div class="form-group">
                        <div
                            class="
                                bootstrap-duallistbox-container
                                row
                                moveonselect
                                moveondoubleclick
                            "
                        >
                            <div class="box1 col-md-6">
                                <form action="simple-results.html">
                                    <div class="input-group">
                                        <input
                                            type="search"
                                            class="form-control"
                                            placeholder="Buscar lote por código fecha o estado"
                                        />
                                        <div class="input-group-append">
                                            <button
                                                type="submit"
                                                class="btn btn-default"
                                            >
                                                <i class="fa fa-search"></i>
                                            </button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <div class="box2 col-md-6">
                                <router-link
                                    to="/batch-add"
                                    active-class="active"
                                >
                                    <button
                                        type="button"
                                        class="btn btn-default"
                                    >
                                        Crear Lote
                                    </button>
                                </router-link>
                            </div>
                        </div>
                    </div>
                    <!-- /.form-group -->
                </div>
            </div>

            <div class="row">
                <!-- /.col -->
                <div class="col-md-12">
                    <div class="card" v-if="list">
                        <div class="card-header">
                            <div class="card-tools">
                                <ul
                                    class="pagination pagination-sm float-right"
                                >
                                    <li class="page-item">
                                        <a class="page-link" href="#">«</a>
                                    </li>
                                    <li class="page-item">
                                        <a class="page-link" href="#">1</a>
                                    </li>
                                    <li class="page-item">
                                        <a class="page-link" href="#">2</a>
                                    </li>
                                    <li class="page-item">
                                        <a class="page-link" href="#">3</a>
                                    </li>
                                    <li class="page-item">
                                        <a class="page-link" href="#">»</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <!-- /.card-header -->
                        <div class="card-body p-0">
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th>Codigo</th>
                                        <th>Fecha</th>
                                        <th>Peso</th>
                                        <th>Estado</th>
                                        <th>Progreso</th>
                                        <th></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr
                                        class="list-group-item"
                                        :class="{active: index == currentIndex}"
                                        v-for="(batch, index) in batchs.items"
                                        :key="index"
                                        @click="setActiveBatch(batch, index)"
                                    >
                                        <td>
                                            {{ batch.code }}
                                        </td>
                                        <td>{{ batch.update_date }}</td>
                                        <td>
                                            {{ batch.weight }}
                                        </td>
                                        <td>
                                            <span
                                                class="badge bg-primary"
                                                v-if="
                                                    batch.state ==
                                                        'RECOLECCION' ||
                                                    batch.state == 'DESPULPADO'
                                                "
                                                >{{ batch.state }}</span
                                            ><span
                                                class="badge bg-secondary"
                                                v-if="
                                                    batch.state ==
                                                        'FERMENTACION' ||
                                                    batch.state == 'LAVADO'
                                                "
                                                >{{ batch.state }}</span
                                            ><span
                                                class="badge bg-success"
                                                v-if="
                                                    batch.state == 'SECADO' ||
                                                    batch.state == 'TRILLADO'
                                                "
                                                >{{ batch.state }}</span
                                            ><span
                                                class="badge bg-info"
                                                v-if="
                                                    batch.state == 'ALMACENADO'
                                                "
                                                >{{ batch.state }}</span
                                            ><span
                                                class="badge bg-danger"
                                                v-if="batch.state == 'TOSTADO'"
                                                >{{ batch.state }}</span
                                            ><span
                                                class="badge bg-warning"
                                                v-if="
                                                    batch.state == 'ETIQUETADO'
                                                "
                                                >{{ batch.state }}</span
                                            >
                                        </td>
                                        <td>
                                            <div class="progress progress-xs">
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 10%"
                                                    v-if="
                                                        batch.state ==
                                                        'RECOLECCION'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 15%"
                                                    v-if="
                                                        batch.state ==
                                                        'DESPULPADO'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 25%"
                                                    v-if="
                                                        batch.state ==
                                                        'FERMENTACION'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 30%"
                                                    v-if="
                                                        batch.state == 'LAVADO'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 40%"
                                                    v-if="
                                                        batch.state == 'SECADO'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 45%"
                                                    v-if="
                                                        batch.state ==
                                                        'TRILLADO'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 50%"
                                                    v-if="
                                                        batch.state ==
                                                        'ALMACENADO'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 75%"
                                                    v-if="
                                                        batch.state == 'TOSTADO'
                                                    "
                                                ></div>
                                                <div
                                                    class="
                                                        progress-bar
                                                        progress-bar-primary
                                                    "
                                                    style="width: 100%"
                                                    v-if="
                                                        batch.state ==
                                                        'ETIQUETADO'
                                                    "
                                                ></div>
                                            </div>
                                        </td>
                                        <td>
                                            <span
                                                class="badge bg-primary"
                                                v-if="
                                                    batch.state == 'RECOLECCION'
                                                "
                                                >10%</span
                                            ><span
                                                class="badge bg-primary"
                                                v-if="
                                                    batch.state == 'DESPULPADO'
                                                "
                                                >15%</span
                                            ><span
                                                class="badge bg-secondary"
                                                v-if="
                                                    batch.state ==
                                                    'FERMENTACION'
                                                "
                                                >25%</span
                                            ><span
                                                class="badge bg-secondary"
                                                v-if="batch.state == 'LAVADO'"
                                                >30%</span
                                            ><span
                                                class="badge bg-success"
                                                v-if="batch.state == 'SECADO'"
                                                >40%</span
                                            ><span
                                                class="badge bg-success"
                                                v-if="batch.state == 'TRILLADO'"
                                                >45%</span
                                            ><span
                                                class="badge bg-info"
                                                v-if="
                                                    batch.state == 'ALMACENADO'
                                                "
                                                >50%</span
                                            ><span
                                                class="badge bg-danger"
                                                v-if="batch.state == 'TOSTADO'"
                                                >75%</span
                                            ><span
                                                class="badge bg-warning"
                                                v-if="
                                                    batch.state == 'ETIQUETADO'
                                                "
                                                >100%</span
                                            >
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <!-- /.card-body -->
                    </div>
                    <!-- /.card -->

                    <!-- /.card -->
                </div>
                <!-- /.col -->
            </div>
        </div>
        <!-- /.container-fluid -->
    </section>
    <!-- UPDATE-->
    <section class="container-fluid pr-5 pl-5" v-if="update">
        <div class="card card-default pr-5 pl-5">
            <div class="card-header p-3 align-self-center">
                <h3 class="card-title">
                    Actualizar el ciclo poscosecha del lote
                </h3>
            </div>
            <!-- /.card-header -->
            <!-- form start -->
            <form>
                <div class="card-body">
                    <div class="form-group">
                        <label for="code">Código</label>
                        <input
                            required
                            disabled
                            type="text"
                            class="form-control"
                            id="code"
                            v-model="currentBatch.code"
                            placeholder="Ingrese un Código"
                        />
                    </div>
                    <div class="form-group">
                        <label for="weight">Peso</label>
                        <input
                            disabled
                            required
                            type="number"
                            class="form-control"
                            id="weight"
                            v-model="currentBatch.weight"
                            v-if="currentBatch.state == 'ETIQUETADO'"
                            placeholder="Ingrese el peso"
                        />
                        <input
                            required
                            type="number"
                            class="form-control"
                            id="weight"
                            v-model="currentBatch.weight"
                            v-if="currentBatch.state != 'ETIQUETADO'"
                            placeholder="Ingrese el peso"
                        />
                    </div>
                    <div class="form-group">
                        <label for="coffe_type">Tipo de Cafe</label>
                        <input
                            required
                            disabled
                            class="form-control"
                            id="coffe_type"
                            v-model="currentBatch.coffe_type"
                            placeholder="Ingrese el tipo de cafe"
                        />
                    </div>
                    <div class="form-group">
                        <label for="varieties">Variedad</label>
                        <input
                            required
                            disabled
                            class="form-control"
                            id="varieties"
                            v-model="currentBatch.varieties"
                            placeholder="Ingrese la variedad"
                        />
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'RECOLECCION'"
                    >
                        <label for="features">Características</label>
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_despulpado_dict.ph_water"
                            placeholder="PH del Agua"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_despulpado_dict.climate"
                            placeholder="Clima (Centígrados)"
                        />
                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_despulpado_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'DESPULPADO'"
                    >
                        <label for="features">Características</label>
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_fermentacion_dict.time"
                            placeholder="Tiempo"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_fermentacion_dict.climate"
                            placeholder="Clima (Centígrados)"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_fermentacion_dict.liters_water"
                            placeholder="Litros de Agua"
                        />
                        <label>Sistema Cerrado</label>
                        <select
                            name="system_close"
                            id="system_close"
                            class="form-control mb-1"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="feature_fermentacion_dict.system_close"
                        >
                            <option value="SI">SI</option>
                            <option value="NO">NO</option>
                        </select>
                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_fermentacion_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'FERMENTACION'"
                    >
                        <label for="features">Características</label>
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_lavado_dict.time"
                            placeholder="Tiempo"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_lavado_dict.liters_water"
                            placeholder="Litros de Agua"
                        />
                        <label>Sistema Cerrado</label>
                        <select
                            name="system_close"
                            id="system_close"
                            class="form-control mb-1"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="feature_lavado_dict.system_close"
                        >
                            <option value="SI">SI</option>
                            <option value="NO">NO</option>
                        </select>
                        <label>Metodo Manual</label>
                        <select
                            name="manual"
                            id="manual"
                            class="form-control mb-1"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="feature_lavado_dict.manual"
                        >
                            <option value="SI">SI</option>
                            <option value="NO">NO</option>
                        </select>
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_lavado_dict.climate"
                            placeholder="Clima (Centigrados)"
                        />
                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_lavado_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'LAVADO'"
                    >
                        <label for="features">Características</label>
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_secado_dict.time"
                            placeholder="Tiempo"
                        />
                        <label>Sistema Cerrado</label>
                        <select
                            name="system_close"
                            id="system_close"
                            class="form-control mb-1"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="feature_secado_dict.system_close"
                        >
                            <option value="SI">SI</option>
                            <option value="NO">NO</option>
                        </select>

                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_secado_dict.climate"
                            placeholder="Clima (Centigrados)"
                        />
                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_secado_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'SECADO'"
                    >
                        <label for="features">Características</label>
                        <br />
                        <label>Metodo Manual</label>
                        <select
                            name="manual"
                            id="manual"
                            class="form-control mb-1"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="feature_trillado_dict.manual"
                        >
                            <option value="SI">SI</option>
                            <option value="NO">NO</option>
                        </select>
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_trillado_dict.time"
                            placeholder="Tiempo"
                        />
                        <label>Sistema Cerrado</label>
                        <select
                            name="system_close"
                            id="system_close"
                            class="form-control mb-1"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="feature_trillado_dict.system_close"
                        >
                            <option value="SI">SI</option>
                            <option value="NO">NO</option>
                        </select>

                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_trillado_dict.climate"
                            placeholder="Clima (Centigrados)"
                        />
                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_trillado_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'TRILLADO'"
                    >
                        <label for="features">Características</label>
                        <input
                            required
                            type="text"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_almacenamiento_dict.type_pergamino"
                            placeholder="Tipo de Pergamino"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_almacenamiento_dict.time"
                            placeholder="Tiempo"
                        />
                        <label>Sistema Cerrado</label>
                        <select
                            name="system_close"
                            id="system_close"
                            class="form-control mb-1"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="feature_almacenamiento_dict.system_close"
                        >
                            <option value="SI">SI</option>
                            <option value="NO">NO</option>
                        </select>

                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_almacenamiento_dict.climate"
                            placeholder="Clima (Centigrados"
                        />
                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_almacenamiento_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'ALMACENADO'"
                    >
                        <label for="features">Características</label>
                        <input
                            required
                            type="text"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_tostado_dict.type_pergamino"
                            placeholder="Tipo de Pergamino"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_tostado_dict.time"
                            placeholder="Tiempo"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_tostado_dict.density"
                            placeholder="Densidad"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_tostado_dict.ph"
                            placeholder="PH"
                        />
                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_almacenamiento_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'TOSTADO'"
                    >
                        <label for="features">Características</label>
                        <input
                            required
                            type="text"
                            class="form-control mb-1"
                            id="features"
                            v-model="feature_empaquetado_dict.type_packing"
                            placeholder="Tipo de Paquete"
                        />

                        <textarea
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="feature_empaquetado_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div
                        class="form-group"
                        v-if="currentBatch.state == 'ETIQUETADO'"
                    >
                        <label for="features">Características</label>
                        <input
                            disabled
                            required
                            type="text"
                            class="form-control mb-1"
                            id="features"
                            v-model="
                                currentBatch.history_etiquetado.ETIQUETADO
                                    .features.type_packing
                            "
                            placeholder="Tipo de Paquete"
                        />

                        <textarea
                            disabled
                            class="form-control"
                            rows="3"
                            id="features"
                            v-model="
                                currentBatch.history_etiquetado.ETIQUETADO
                                    .features.more_features
                            "
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div class="form-group">
                        <label for="state">Estado Actual </label>
                        <input
                            required
                            disabled
                            type="text"
                            class="form-control"
                            id="state"
                            v-model="currentBatch.state"
                            placeholder="Ingrese el Estado"
                        />
                    </div>
                </div>
                <!-- /.card-body -->

                <div class="card-footer float-right">
                    <button
                        @click="deleteBatch"
                        type="submit"
                        class="btn btn-danger"
                    >
                        Eliminar
                    </button>
                    <button
                        @click="updateBatch"
                        type="submit"
                        class="btn btn-primary ml-2"
                    >
                        Guardar
                    </button>
                </div>
            </form>
        </div>
    </section>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import BatchDataService from '@/services/BatchDataService';
import Batch from '@/types/Batch';
import ResponseData from '@/types/ResponseData';
import {useToast} from 'vue-toastification';
import NotifyDataService from '@/services/NotifyDataService';

let toast = useToast();
export default defineComponent({
    name: 'batchs-list',
    data() {
        return {
            batchs: [] as Batch[],
            currentBatch: {} as Batch,
            currentIndex: -1,
            update: false,
            list: true,
            title: '',
            feature_despulpado_dict: {
                ph_water: null,
                climate: null,
                more_features: ''
            },
            feature_fermentacion_dict: {
                time: null,
                liters_water: null,
                system_close: '',
                climate: null,
                more_features: ''
            },
            feature_lavado_dict: {
                time: null,
                liters_water: null,
                system_close: '',
                manual: 'Boolean',
                climate: null,
                more_features: ''
            },
            feature_secado_dict: {
                time: null,
                system_close: Boolean,
                climate: null,
                more_features: ''
            },
            feature_trillado_dict: {
                manual: Boolean,
                time: null,
                system_close: Boolean,
                climate: null,
                more_features: ''
            },
            feature_almacenamiento_dict: {
                type_pergamino: '',
                time: null,
                system_close: Boolean,
                climate: null,
                more_features: ''
            },
            feature_tostado_dict: {
                type_pergamino: '',
                time: null,
                density: null,
                ph: null,
                more_features: ''
            },
            feature_empaquetado_dict: {
                type_packing: '',
                more_features: ''
            }
        };
    },
    methods: {
        retrieveBatch() {
            BatchDataService.getAll()
                .then((response: ResponseData) => {
                    this.batchs = response.data;
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        },
        updateBatch() {
            let message_text = '';
            let payload = {
                id: this.currentBatch.id,
                code: this.currentBatch.code,
                weight: this.currentBatch.weight,
                coffe_type: this.currentBatch.coffe_type,
                varieties: this.currentBatch.varieties,
                state: this.currentBatch.state,
                contact: this.currentBatch.contact,
                contact_name: this.currentBatch.contact_name,
                features: {}
            };
            if (this.currentBatch.state == 'RECOLECCION') {
                payload.features = this.feature_despulpado_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO DESPULPADO';
            }
            if (this.currentBatch.state == 'DESPULPADO') {
                payload.features = this.feature_fermentacion_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO FERMENTACION';
            }
            if (this.currentBatch.state == 'FERMENTACION') {
                payload.features = this.feature_lavado_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO LAVADO';
            }
            if (this.currentBatch.state == 'LAVADO') {
                payload.features = this.feature_secado_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO SECADO';
            }
            if (this.currentBatch.state == 'SECADO') {
                payload.features = this.feature_trillado_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO TRILLADO';
            }
            if (this.currentBatch.state == 'TRILLADO') {
                payload.features = this.feature_almacenamiento_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO ALMACENADO';
            }
            if (this.currentBatch.state == 'ALMACENADO') {
                payload.features = this.feature_tostado_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO TOSTADO';
            }
            if (this.currentBatch.state == 'TOSTADO') {
                payload.features = this.feature_empaquetado_dict;
                message_text =
                    'Notificación Cafetero su Lote esta en ESTADO ETIQUETADO';
            }
            if (this.currentBatch.state == 'ETIQUETADO') {
                payload.features = this.currentBatch.features;
            }
            BatchDataService.update(payload.id, payload)
                .then((response: ResponseData) => {
                    this.currentBatch.id = response.data.id;
                    toast.success('El Lote fue Actualizado');
                })
                .catch((e: Error) => {
                    console.log(e);
                });
            let notify = {
                contact: payload.contact,
                message: message_text
            };
            NotifyDataService.send(notify)
                .then((response: ResponseData) => {
                    console.log(response.data);
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        },
        deleteBatch() {
            BatchDataService.delete(this.currentBatch.id)
                .then((response: ResponseData) => {
                    toast.error('El Lote fue Eliminado');
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        },
        refreshList() {
            this.retrieveBatch();
            this.currentBatch = {} as Batch;
            this.currentIndex = -1;
        },
        setActiveBatch(batch: Batch, index = -1) {
            this.currentBatch = batch;
            this.currentIndex = index;
            this.update = true;
            this.list = false;
        },
        setDesactiveBatch() {
            this.update = false;
            this.list = true;
        },
        removeAllBatch() {
            BatchDataService.deleteAll()
                .then((response: ResponseData) => {
                    this.refreshList();
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        }
    },
    mounted() {
        this.retrieveBatch();
    }
});
</script>

<style lang="scss" scoped>
.list-group-item {
    display: table-row !important;
}
</style>