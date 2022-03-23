"""Add foreign-key to posts table

Revision ID: 274102f6b508
Revises: 07d8be217356
Create Date: 2022-03-23 11:45:46.854372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '274102f6b508'
down_revision = '07d8be217356'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
