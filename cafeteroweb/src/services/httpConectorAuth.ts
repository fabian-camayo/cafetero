import AuthDataService from "@/services/AuthDataService";

export const accessToken = (username: string, password: string) => {
    return AuthDataService.create({username,password})
    .then()
    .catch((e: Error) => {
                console.log(e);
    });
}