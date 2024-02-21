# Doc

[Julep Python SDK Index](../../README.md#julep-python-sdk-index) / [Julep](../index.md#julep) / [Managers](./index.md#managers) / Doc

> Auto-generated documentation for [julep.managers.doc](../../../../../../julep/managers/doc.py) module.

- [Doc](#doc)
  - [AsyncDocsManager](#asyncdocsmanager)
  - [BaseDocsManager](#basedocsmanager)
  - [DocsManager](#docsmanager)

## AsyncDocsManager

[Show source in doc.py:327](../../../../../../julep/managers/doc.py#L327)

A class for managing asynchronous operations on documents.

Inherits from BaseDocsManager to provide async document retrieval, creation, and deletion.

#### Attributes

Inherited from BaseDocsManager.

#### Methods

async get(self, *, agent_id: Optional[Union[str, UUID]] = None, user_id: Optional[Union[str, UUID]] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> List[Doc]:
    Asynchronously get a list of documents, with optional filtering based on agent_id, user_id, and pagination options limit and offset.

#### Arguments

agent_id (Optional[Union[str, UUID]]): The agent's identifier to filter documents.
user_id (Optional[Union[str, UUID]]): The user's identifier to filter documents.
- `limit` *Optional[int]* - The maximum number of documents to return.
- `offset` *Optional[int]* - The offset from where to start returning documents.
agent_id (Optional[Union[str, UUID]]): The agent's identifier associated with the document.
user_id (Optional[Union[str, UUID]]): The user's identifier associated with the document.
- `doc` *DocDict* - The document data to be created.
doc_id (Union[str, UUID]): The unique identifier of the document to be deleted.
agent_id (Optional[Union[str, UUID]]): The agent's identifier associated with the document, if applicable.
user_id (Optional[Union[str, UUID]]): The user's identifier associated with the document, if applicable.

#### Returns

- `List[Doc]` - A list of documents.

async create(self, *, agent_id: Optional[Union[str, UUID]] = None, user_id: Optional[Union[str, UUID]] = None, doc: DocDict) -> ResourceCreatedResponse:
    Asynchronously create a new document with the given document information, and optional agent_id and user_id.
        - `ResourceCreatedResponse` - A response object indicating successful creation of the document.

async delete(self, *, doc_id: Union[str, UUID], agent_id: Optional[Union[str, UUID]] = None, user_id: Optional[Union[str, UUID]] = None):
    Asynchronously delete a document by its id, with optional association to a specific agent_id or user_id.

#### Notes

The `@beartype` decorator is being used to perform runtime type checking on the function arguments.

#### Signature

```python
class AsyncDocsManager(BaseDocsManager): ...
```

#### See also

- [BaseDocsManager](#basedocsmanager)

### AsyncDocsManager().create

[Show source in doc.py:406](../../../../../../julep/managers/doc.py#L406)

Create a new resource asynchronously.

#### Arguments

agent_id (Optional[Union[str, UUID]]): The ID of the agent. Default is None.
user_id (Optional[Union[str, UUID]]): The ID of the user. Default is None.
- `doc` *DocDict* - A dictionary containing document data.

#### Returns

- `ResourceCreatedResponse` - An object representing the response for a resource created.

#### Raises

- `BeartypeException` - If any of the input arguments do not match their expected types. This is implicitly raised due to the use of the beartype decorator.

#### Signature

```python
@beartype
async def create(
    self,
    agent_id: Optional[Union[str, UUID]] = None,
    user_id: Optional[Union[str, UUID]] = None,
    doc: DocDict,
) -> ResourceCreatedResponse: ...
```

### AsyncDocsManager().delete

[Show source in doc.py:434](../../../../../../julep/managers/doc.py#L434)

Asynchronously deletes a document by its ID.

This function is a coroutine and must be awaited.

#### Arguments

doc_id (Union[str, UUID]): The unique identifier of the document to delete.
agent_id (Optional[Union[str, UUID]]): The unique identifier of the agent, if any.
user_id (Optional[Union[str, UUID]]): The unique identifier of the user, if any.

#### Returns

- `Coroutine[Any]` - A coroutine that, when awaited, returns the result of the document deletion process.

#### Notes

The `@beartype` decorator is used to enforce type checking on the function arguments.

#### Signature

```python
@beartype
async def delete(
    self,
    doc_id: Union[str, UUID],
    agent_id: Optional[Union[str, UUID]] = None,
    user_id: Optional[Union[str, UUID]] = None,
): ...
```

### AsyncDocsManager().get

[Show source in doc.py:367](../../../../../../julep/managers/doc.py#L367)

Asynchronously get a list of documents.

This function fetches documents based on the provided filtering criteria such as `agent_id`, `user_id`,
and supports pagination through `limit` and `offset`.

#### Arguments

agent_id (Optional[Union[str, UUID]]): The ID of the agent to filter documents by. Default is None.
user_id (Optional[Union[str, UUID]]): The ID of the user to filter documents by. Default is None.
- `limit` *Optional[int]* - The maximum number of documents to return. Default is None.
- `offset` *Optional[int]* - The offset from where to start the document retrieval. Default is None.

#### Returns

- `List[Doc]` - A list of document objects.

#### Notes

The `@beartype` decorator is used to ensure that arguments conform to the expected types.

#### Raises

- `BeartypeDecorHintPepParamException` - If any of the parameters do not adhere to the declared types.

#### Signature

```python
@beartype
async def get(
    self,
    agent_id: Optional[Union[str, UUID]] = None,
    user_id: Optional[Union[str, UUID]] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[Doc]: ...
```



## BaseDocsManager

[Show source in doc.py:19](../../../../../../julep/managers/doc.py#L19)

Manages documents for agents or users by providing methods to get, create, and delete docsrmation.

The class utilizes an API client to interact with a back-end service that handles the document management operations.

Typical usage example:

docs_manager = BaseDocsManager(api_client)
agent_docs = docs_manager._get(agent_id="some-agent-uuid")
user_docs = docs_manager._get(user_id="some-user-uuid")
created_doc = docs_manager._create(agent_id="some-agent-uuid", doc={"key": "value"})
docs_manager._delete(user_id="some-user-uuid", doc_id="some-doc-uuid")

#### Attributes

- `api_client` - A client instance used to make API calls to the document management system.

#### Methods

- `_get(agent_id` - Optional[Union[str, UUID]], user_id: Optional[Union[str, UUID]],
     - `limit` - Optional[int]=None, offset: Optional[int]=None) -> Union[GetAgentDocsResponse, Awaitable[GetAgentDocsResponse]]
    Retrieves docsrmation for either an agent or user.
    Must provide exactly one valid UUID v4 for either `agent_id` or `user_id`.

- `_create(agent_id` - Optional[Union[str, UUID]], user_id: Optional[Union[str, UUID]], doc: DocDict) -> Union[ResourceCreatedResponse, Awaitable[ResourceCreatedResponse]]
    Creates docsrmation for either an agent or user.
    Must provide exactly one valid UUID v4 for either `agent_id` or `user_id`.
    The `doc` parameter contains the document information to be created.

- `_delete(agent_id` - Optional[Union[str, UUID]], user_id: Optional[Union[str, UUID]], doc_id: Union[str, UUID]):
    Deletes docsrmation for either an agent or user.
    Must provide exactly one valid UUID v4 for either `agent_id` or `user_id`, and a valid UUID for `doc_id`.

#### Signature

```python
class BaseDocsManager(BaseManager): ...
```

### BaseDocsManager()._create

[Show source in doc.py:98](../../../../../../julep/managers/doc.py#L98)

Create a new resource with docsrmation for either an agent or a user, but not both.

This function asserts that exactly one of `agent_id` or `user_id` is provided and is a valid UUID v4.
It then creates the appropriate docsrmation based on which ID was provided.

Args:
    agent_id (Optional[Union[str, UUID]]): The UUID of the agent or None.
    user_id (Optional[Union[str, UUID]]): The UUID of the user or None.
    doc (DocDict): A dictionary containing the document data for the resource being created.

Returns:
    Union[ResourceCreatedResponse, Awaitable[ResourceCreatedResponse]]: The response after creating the resource, which could be immediate or an awaitable for asynchronous execution.

Raises:
    AssertionError: If both `agent_id` and `user_id` are provided, neither are provided, or if the provided IDs are not valid UUID v4 strings.

Note:
    One and only one of `agent_id` or `user_id` must be provided and must be a valid UUID v4.
    The `DocDict` type should be a dictionary compatible with the `CreateDoc` schema.

#### Signature

```python
def _create(
    self,
    agent_id: Optional[Union[str, UUID]],
    user_id: Optional[Union[str, UUID]],
    doc: DocDict,
) -> Union[ResourceCreatedResponse, Awaitable[ResourceCreatedResponse]]: ...
```

### BaseDocsManager()._delete

[Show source in doc.py:145](../../../../../../julep/managers/doc.py#L145)

Delete docs based on either an agent_id or a user_id.

This method selects the appropriate deletion operation (agent or user) based on whether an `agent_id` or `user_id` is provided. Only one of these ID types should be valid and provided.

Args:
    agent_id (Optional[Union[str, UUID]]): A unique identifier of an agent. Either a string or UUID v4, but not both `agent_id` and `user_id`.
    user_id (Optional[Union[str, UUID]]): A unique identifier of a user. Either a string or UUID v4, but not both `agent_id` and `user_id`.
    doc_id (Union[str, UUID]): A unique identifier for docsrmation to be deleted, as a string or UUID v4.

Returns:
    The result of the API deletion request. This can be the response object from the client's delete operation.

Raises:
    AssertionError: If neither `agent_id` nor `user_id` is valid, if both are provided simultaneously, or if negation logic for valid UUIDs fails.
    Other exceptions related to the `api_client` operations could potentially be raised and depend on its implementation.

#### Signature

```python
def _delete(
    self,
    agent_id: Optional[Union[str, UUID]],
    user_id: Optional[Union[str, UUID]],
    doc_id: Union[str, UUID],
): ...
```

### BaseDocsManager()._get

[Show source in doc.py:52](../../../../../../julep/managers/doc.py#L52)

Retrieve docsrmation for an agent or user based on their ID.

This internal method fetches docsrmation for either an agent or a user,
but not both. If both or neither `agent_id` and `user_id` are provided, it will
assert an error.

#### Arguments

agent_id (Optional[Union[str, UUID]]): The UUID v4 of the agent for whom docs is requested, exclusive with `user_id`.
user_id (Optional[Union[str, UUID]]): The UUID v4 of the user for whom docs is requested, exclusive with `agent_id`.
- `limit` *Optional[int]* - The maximum number of records to return. Defaults to None.
- `offset` *Optional[int]* - The number of records to skip before starting to collect the response set. Defaults to None.

#### Returns

- `Union[GetAgentDocsResponse,` *Awaitable[GetAgentDocsResponse]]* - The response object containing docsrmation about the agent or user, or a promise of such an object if the call is asynchronous.

#### Raises

- `AssertionError` - If both `agent_id` and `user_id` are provided or neither is provided, or if the provided IDs are not valid UUID v4.

#### Signature

```python
def _get(
    self,
    agent_id: Optional[Union[str, UUID]],
    user_id: Optional[Union[str, UUID]],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Union[GetAgentDocsResponse, Awaitable[GetAgentDocsResponse]]: ...
```



## DocsManager

[Show source in doc.py:187](../../../../../../julep/managers/doc.py#L187)

A class responsible for managing documents.

This class provides methods for retrieving, creating, and deleting documents. It uses a base document management system to perform operations.

#### Attributes

None specific to this class, as all are inherited from BaseDocsManager.

#### Methods

get:
    Retrieves a list of documents according to specified filters.

#### Arguments

agent_id (Optional[Union[str, UUID]]): The agent's identifier to filter documents by, if any.
user_id (Optional[Union[str, UUID]]): The user's identifier to filter documents by, if any.
- `limit` *Optional[int]* - The maximum number of documents to be retrieved.
- `offset` *Optional[int]* - The number of documents to skip before starting to collect the document output list.

agent_id (Optional[Union[str, UUID]]): The agent's identifier associated with the document, if any.
user_id (Optional[Union[str, UUID]]): The user's identifier associated with the document, if any.
- `doc` *DocDict* - The document to be created represented as a dictionary of document metadata.

doc_id (Union[str, UUID]): The identifier of the document to be deleted.
agent_id (Optional[Union[str, UUID]]): The agent's identifier associated with the document, if any.
user_id (Optional[Union[str, UUID]]): The user's identifier associated with the document, if any.

#### Returns

- `List[Doc]` - A list of documents matching the provided filters.

create:
    Creates a new document.

- `ResourceCreatedResponse` - An object representing the creation response, typically containing the ID of the created document.

delete:
    Deletes a document by its document identifier.

None, but the method may raise exceptions on failure.

#### Signature

```python
class DocsManager(BaseDocsManager): ...
```

#### See also

- [BaseDocsManager](#basedocsmanager)

### DocsManager().create

[Show source in doc.py:265](../../../../../../julep/managers/doc.py#L265)

Create a new resource with the specified document.

This method wraps a call to an internal '_create' method, passing along any
specified agent or user identifiers, along with the document data.

#### Arguments

agent_id (Optional[Union[str, UUID]]): The agent identifier associated with the resource creation.
user_id (Optional[Union[str, UUID]]): The user identifier associated with the resource creation.
- `doc` *DocDict* - A dictionary containing the document data.

#### Returns

- `ResourceCreatedResponse` - An object representing the response for the resource creation operation.

#### Raises

- `BeartypeException` - If any input parameters are of incorrect type, due to type enforcement by the @beartype decorator.

#### Signature

```python
@beartype
def create(
    self,
    agent_id: Optional[Union[str, UUID]] = None,
    user_id: Optional[Union[str, UUID]] = None,
    doc: DocDict,
) -> ResourceCreatedResponse: ...
```

### DocsManager().delete

[Show source in doc.py:296](../../../../../../julep/managers/doc.py#L296)

Deletes a document by its identifier.

This function wraps the internal _delete method, providing an interface to delete documents by their ID while optionally specifying the agent ID and user ID.

#### Arguments

doc_id (Union[str, UUID]): The unique identifier of the document to be deleted.
agent_id (Optional[Union[str, UUID]]): The unique identifier of the agent performing the delete operation, if any.
user_id (Optional[Union[str, UUID]]): The unique identifier of the user performing the delete operation, if any.

#### Returns

The return type depends on the implementation of the `_delete` method.

#### Raises

The exceptions raised depend on the implementation of the `_delete` method.

#### Signature

```python
@beartype
def delete(
    self,
    doc_id: Union[str, UUID],
    agent_id: Optional[Union[str, UUID]] = None,
    user_id: Optional[Union[str, UUID]] = None,
): ...
```

### DocsManager().get

[Show source in doc.py:232](../../../../../../julep/managers/doc.py#L232)

Retrieve a list of documents based on specified criteria.

This method supports filtering the documents by agent_id or user_id, and also supports pagination through the limit and offset parameters.

#### Arguments

agent_id (Optional[Union[str, UUID]]): The unique identifier for the agent. Can be a string or a UUID object. Default is None, which means no filtering by agent_id is applied.
user_id (Optional[Union[str, UUID]]): The unique identifier for the user. Can be a string or a UUID object. Default is None, which means no filtering by user_id is applied.
- `limit` *Optional[int]* - The maximum number of documents to retrieve. Default is None, which means no limit is applied.
- `offset` *Optional[int]* - The number of documents to skip before starting to collect the document list. Default is None, which means no offset is applied.

#### Returns

- `List[Doc]` - A list of documents that match the provided criteria.

#### Notes

The `@beartype` decorator is used to ensure that the input arguments are of the expected types. If an argument is passed that does not match the expected type, a type error will be raised.

#### Signature

```python
@beartype
def get(
    self,
    agent_id: Optional[Union[str, UUID]] = None,
    user_id: Optional[Union[str, UUID]] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[Doc]: ...
```