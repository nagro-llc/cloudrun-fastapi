"""add relationships

Revision ID: e00b83f8ea20
Revises: fcab48b94915
Create Date: 2020-03-31 21:56:58.961478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e00b83f8ea20'
down_revision = 'fcab48b94915'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(op.f('fk_items_user_id_users'), 'items', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_items_user_id_users'), 'items', type_='foreignkey')
    op.drop_column('items', 'user_id')
    # ### end Alembic commands ###
