// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

export type PeopleAction = FindPersonAction | FindPersonsManagerAction;

export type FindPersonAction = {
    actionName: "findPerson";
    parameters: {
        name: string; // can be first name, last name, or full name
    };
};

export type FindPersonsManagerAction = {
    actionName: "findPersonsManager";
    parameters: {
        userId: string; // can be fetched with the "findPerson" action
    };
};
