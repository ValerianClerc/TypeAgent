# Copyright (c) Microsoft Corporation and Henry Lucco.
# Licensed under the MIT License.

def get_knowledge_prompt(message: str) -> str:
    template = "You are a service that translates user messages in a conversation into JSON objects of type \"KnowledgeResponse\" according to the following TypeScript definitions:\n```\n\n\nexport type Quantity = {\n    amount: number;\n    units: string;\n};\nexport type Value = string | number | boolean | Quantity;\nexport type Facet = {\n    name: string;\n    // Very concise values.\n    value: Value;\n};\n// Specific, tangible people, places, institutions or things only\nexport type ConcreteEntity = {\n    // the name of the entity or thing such as \"Bach\", \"Great Gatsby\", \"frog\" or \"piano\"\n    name: string;\n    // the types of the entity such as \"speaker\", \"person\", \"artist\", \"animal\", \"object\", \"instrument\", \"school\", \"room\", \"museum\", \"food\" etc.\n    // An entity can have multiple types; entity types should be single words\n    type: string[];\n    // A specific, inherent, defining, or non-immediate facet of the entity such as \"blue\", \"old\", \"famous\", \"sister\", \"aunt_of\", \"weight: 4 kg\"\n    // trivial actions or state changes are not facets\n    // facets are concise \"properties\"\n    facets?: Facet[];\n};\nexport type ActionParam = {\n    name: string;\n    value: Value;\n};\nexport type VerbTense = \"past\" | \"present\" | \"future\";\nexport type Action = {\n    // Each verb is typically a word\n    verbs: string[];\n    verbTense: VerbTense;\n    subjectEntityName: string | \"none\";\n    objectEntityName: string | \"none\";\n    indirectObjectEntityName: string | \"none\";\n    params?: (string | ActionParam)[];\n    // If the action implies this additional facet or property of the subjectEntity, such as hobbies, activities, interests, personality\n    subjectEntityFacet?: Facet | undefined;\n};\n// Detailed and comprehensive knowledge response\nexport type KnowledgeResponse = {\n    entities: ConcreteEntity[];\n    // The 'subjectEntityName' and 'objectEntityName' must correspond to the 'name' of an entity listed in the 'entities' array.\n    actions: Action[];\n    // Some actions can ALSO be expressed in a reverse way... e.g. (A give to B) --> (B receive from A) and vice versa\n    // If so, also return the reverse form of the action, full filled out\n    inverseActions: Action[];\n    // Detailed, descriptive topics and keyword.\n    topics: string[];\n};\n\n```\nThe following are messages in a conversation:\n\"\"\"\n<<message>>\n\"\"\"\nThe following is the user request translated into a JSON object with 2 spaces of indentation and no properties with the value undefined:\n"
    return template.replace("<<message>>", message)