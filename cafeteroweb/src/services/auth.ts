/* eslint-disable @typescript-eslint/explicit-module-boundary-types */

import {accessToken} from './httpConectorAuth'

const getError = (error: any) => {
    const message =
        (error &&
            error.response &&
            error.response.data &&
            error.response.data.message) ||
        'Failed';
    return new Error(message);
};

export const loginByAuth = async (email: string, password: string) => {
    try {
        const token = accessToken(email, password);
        return token.then(response => response.data.token);
    } catch (error: any) {
        throw getError(error);
    }
};

export const registerByAuth = async (email: string, password: string) => {
    try {
        return 'token';
    } catch (error: any) {
        throw getError(error);
    }
};

export const getProfile = async () => {
    try {
        return "prueba";
    } catch (error: any) {
        throw getError(error);
    }
};