# pylint: disable=no-member,unused-argument
import graphene


class GlobalInterface(graphene.Interface):
    """Global interface for objects with a unique ID.

    This interface defines a field `uuid` of type `graphene.UUID` and a resolver function
    `resolve_id` that returns the `uuid` attribute of the object being queried.

    Any GraphQL type that implements this interface must include a field `uuid` of type
    `graphene.UUID` and a resolver function `resolve_uuid` that returns the `uuid` attribute
    of the object being queried.
    """
    uuid = graphene.UUID(required=True)
    
    def resolve_uuid(self, info):
        """Resolve the `uuid` field of the object being queried.

        This resolver function returns the `uuid` attribute of the object being queried.

        Args:
            info (graphene.ResolveInfo): Information about the current execution context.

        Returns:
            uuid: The `uuid` attribute of the object being queried.
        """
        return self.uuid
