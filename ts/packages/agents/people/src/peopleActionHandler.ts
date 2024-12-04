// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

import { ActionContext, AppAgent, AppAction } from "@typeagent/agent-sdk";
import { createActionResult } from "@typeagent/agent-sdk/helpers/action";

import { PeopleAction } from "./peopleActionsSchema.js";
import {
    CommandHandlerNoParams,
    CommandHandlerTable,
    getCommandInterface,
} from "@typeagent/agent-sdk/helpers/command";
import chalk from "chalk";

export function instantiate(): AppAgent {
    return {
        executeAction: executePeopleAction,
        ...getCommandInterface(handlers),
    };
}

export class PeopleCommandHandler implements CommandHandlerNoParams {
    public readonly description =
        "Have the agent generate a personalized greeting.";
    public async run(context: ActionContext) {
        chalk.yellow('Calling via "run" method');
        const text = "Hello!";
        context.actionIO.setDisplay(text);
    }
}

const handlers: CommandHandlerTable = {
    description: "Look up information about people and their managers",
    defaultSubCommand: new PeopleCommandHandler(),
    commands: {},
};

async function executePeopleAction(action: AppAction, context: ActionContext) {
    let result = await handlePeopleAction(action as PeopleAction, context);
    return result;
}

async function handlePeopleAction(
    action: PeopleAction,
    context: ActionContext,
) {
    chalk.yellow('Calling via "handlePeopleAction" method');
    switch (action.actionName) {
        case "findPerson": {
            return createActionResult(
                // "Looking up person: " + action.parameters.name,
                "The user's email is test123@microsoft.com, and their user ID is 123456789",
            );
        }
        case "findPersonsManager": {
            return createActionResult(
                "Looking up manager for user: " + action.parameters.userId,
            );
        }
        default:
            throw new Error(`Unknown action: ${action}`);
    }
}
