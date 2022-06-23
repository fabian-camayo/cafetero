<template >
    <li class="nav-item dropdown user-menu" ref="dropdown">
        <button
            @click="toggleDropdown"
            class="nav-link dropdown-toggle"
            data-toggle="dropdown"
        >
            <img
                :src="
                    user && user.picture
                        ? user.picture
                        : require('@/assets/img/default-profile.png')
                "
                class="user-image img-circle elevation-2"
                alt="User Image"
            />
        </button>
        <ul
            class="dropdown-menu dropdown-menu-lg dropdown-menu-right"
            :class="{show: isDropdownOpened}"
        >
            <!-- User image -->
            <li class="user-header bg-primary">
                <img
                    :src="
                        user && user.picture
                            ? user.picture
                            : require('@/assets/img/default-profile.png')
                    "
                    class="img-circle elevation-2"
                    alt="User Image"
                />

                <p>
                    <span>{{ user && user.email }}</span>
                    <small>
                        <span>Member since </span>
                        <span>Nov. 2012</span>
                    </small>
                </p>
            </li>
            <!-- Menu Body -->

            <!-- Menu Footer-->
            <li class="user-footer">
                <router-link
                    to="/profile"
                    class="btn btn-default btn-flat"
                    @click="isDropdownOpened = false"
                >
                    Perfil
                </router-link>
                <button
                    @click="logout"
                    class="btn btn-default btn-flat float-right"
                >
                    Salir
                </button>
            </li>
        </ul>
    </li>
</template>
<script lang="ts">
import {IUser} from '@/interfaces/user';
import {Options, Vue} from 'vue-class-component';

@Options({})
export default class User extends Vue {
    private isDropdownOpened = false;

    public mounted(): void {
        document.addEventListener('click', this.documentClick);
    }

    public unmounted(): void {
        document.removeEventListener('click', this.documentClick);
    }

    private toggleDropdown() {
        this.isDropdownOpened = !this.isDropdownOpened;
    }

    private documentClick(event: Event) {
        const el: HTMLElement = this.$refs.dropdown as HTMLElement;
        const target: HTMLElement = event.target as HTMLElement;
        if (el !== target && !el.contains(target)) {
            this.isDropdownOpened = false;
        }
    }

    get user(): IUser {
        return this.$store.getters.user;
    }

    private logout() {
        this.$store.dispatch('logout');
    }
}
</script>
<style lang="scss">
.user-menu {
    .user-image {
        width: 1.6rem !important;
        height: 1.6rem !important;
    }
}
</style>